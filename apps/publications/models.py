from django.db import models
from django.db.models import Q
from django.db.models import Count
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from apps.users.models import UserProfile

"""Consideraciones de las clases Manager: dado que se utiliza un soft delete,
los registros que se retornan siempre deben estar filtrados por su respectivo
campo que indica si fue eliminado o no (por lo general, el campo active).
Por cuestiones de practicidad se podria modificar el metodo get_query_set de
cada manager para que retorne siempre registros no eliminados, sin embargo trae
complicaciones por ejemplo cuando los administradores quieren acceder a esos
registros, o en los chapters cuando se requiere un chapter eliminado para
conectar como nodo intermedio entre otros dos. Hasta encontrar una solucion que
no comprometa los resultados de las busquedas, cada consulta debe asegurarse
de retornar registros no eliminados segun corresponda."""


class ChapterQuery(models.QuerySet):
    """ ChapterQuery sirve para abstraer los filtros que se usan en
    ChapterManager"""

    def public(self):
        return self.filter(~Q(mainStory__status=Permission.NR))

    def active(self):
        return self.filter(active=True)

    def title(self, title):
        return self.filter(title__icontains=title)

    def tags(self, tag):
        q = Q()
        for t in tag.split():
            q |= Q(tag__tag__icontains=t)
        return self.filter(q)

    def first_chapter(self):
        """Filtra los primeros capitulos. (los que no tienen capitulos previos)."""
        return self.filter(prevChapter__isnull=True)

    def by_story(self, idStory):
        """Filtra los capitulo pertenecientes a una story con id = idStory"""
        return self.filter(mainStory=idStory)

    def by_chapter(self, idChapter):
        """Filtra los chapters pertenecientes a otro chapter con prevChapter = idChapter.
        (Las continuaciones de un chapters)"""
        return self.filter(prevChapter=idChapter)

    def by_user(self, userProfile):
        """retorna los chapter de un usuario"""
        return self.filter(own_user=userProfile)


class ChapterManager(models.Manager):
    """La clase ChapterManager sirve para abstraer las consultas que se usan en las views"""

    def get_queryset(self):
        return ChapterQuery(self.model, using=self._db)

    def get_by_title(self, title):
        return self.get_queryset().active().title(title)

    def get_chapters_by_user(self, ownerUser, user):
        """Retorna los chapter de ownerUser. Si ownerUser y user son el mismo, entonces
        retorna todos los chapters de ownerUser, en caso contrario solo retorna
        los chapters publicos."""
        if ownerUser == user:
            return self.get_queryset().by_user(ownerUser.profile.get()).active()
        else:
            return self.get_queryset().by_user(ownerUser.profile.get()).active().public()

    def story_continuations(self, idStory, user):
        """Retorna los primeros capitulos de una Story (las primeras continuaciones)"""
        return self.get_queryset().by_story(idStory).first_chapter().active()

    def chapter_continuations(self, idChapter, user):
        """Retorna las continuaciones de un chapter"""
        return self.get_queryset().by_chapter(idChapter).active()


class StoryPublicationQuery(models.QuerySet):
    """ StoryPublicationQuery sirve para abstraer los filtros que se usan en StoryPublicationManager"""

    def publicOrOwner(self, userProfile):
        """Retorna las stories publicas.
        Si el usuario que hace la consulta es el duenio de la story tambien retorna las privadas.
        Si se conocen ambos usuarios antes de ejecutar la consulta entonces no usar este filtro
        porque es mas ineficiente que preguntar si los usuarios son los mismos.
        Ver get_stories_by_user() como ejemplo."""

        q1 = ~Q(status=Permission.NR)
        q2 = Q(own_user=userProfile)
        return self.filter(q1 | q2)

    def by_user(self, userProfile):
        """retorna las stories de un usuario"""
        return self.filter(own_user=userProfile)

    def public(self):
        return self.filter(~Q(status=Permission.NR))

    def active(self):
        return self.filter(active=True)

    def title(self, title):
        return self.filter(title__icontains=title)

    def tags(self, tag):
        q = Q()
        for t in tag.split():
            q |= Q(tag__tag__icontains=t)
        return self.filter(q)


class StoryPublicationManager(models.Manager):
    """StoryPublicationManager sirve para abstraer las consultas que se usan en las views"""
    def get_queryset(self):
        return StoryPublicationQuery(self.model, using=self._db)

    def get_by_title(self, title):
        return self.get_queryset().active().title(title)

    def get_stories_by_user(self, ownerUser, user):
        ""retorna las stories de ownerUser. Si ownerUser y user son el mismo, entonces
        retorna todas las stories de ownerUser, en caso contrario solo retorna
        las stories publicas.""
        if ownerUser == user:
            return self.get_queryset().by_user(ownerUser.profile.get()).active()
        else:
            return self.get_queryset().by_user(ownerUser.profile.get()).active().public()

    def publications_hall(self, title, tags):
        """retorna las publicaciones que se van a visualizar en el hall por defecto. 
        tambien agrega los filtros necesarios por titulo y tags.
        La consulta implica: publicaciones activas y publicas, que contengan el titulo o al menos
        un tag. Se ordenan por cantidad de tags que tenga cada story de manera descendente y por fecha.
        Osea las que tienen igual cantidad de tags se organizan entre si por fecha, las
        menos recientes primero"""

        qs = self.get_queryset().active().public()
        if title is not "" and title is not None:
            qs = qs.title(title)
        if tags is not "" and tags is not None:
            qs = qs.tags(tags)
            qs = qs.annotate(count=Count("tag")).order_by("-count")
        qs = qs.order_by("date_time")
        return qs.distinct()


def get_upload_path(instance, filename):
    return "publications/user_profile_{0}/{1}".format(instance.own_user.id, filename)


class Permission(models.TextChoices):
    WR = "WR", _("""Leer y Continuar: permite que otros usuarios puedan leer
    la publicación y continuar la trama.""")
    R = "R", _("Solo leer: permite que otros usuarios solo puedan leer la publicación.")
    NR = "NR", _("No ver: solo tú podrás ver esta publicación.")


class StoryPublication(models.Model):
    """Story Publication (root of tree stories)"""

    # datos usuario
    own_user = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    # contenido
    title = models.CharField(max_length=120)
    text_content = models.TextField(max_length=2000)
    # img_content_link = models.URLField(max_length=500)
    img_content_link = models.ImageField(upload_to=get_upload_path, default="gallery/no-img.png")
    active = models.BooleanField(default=True)  # si es una publicacion activa o no.
    date_time = models.DateField(auto_now_add=True)
    views = models.IntegerField(default=0)  # cantidad de visitas
    valoration = models.IntegerField(default=0)
    tag = models.ManyToManyField("Tag")
    color = models.CharField(max_length=7, default="#4a4a4a")
    like = models.ManyToManyField(UserProfile, through="StoryLike",
            related_name="storyLikes", symmetrical=False)
    status = models.CharField(max_length=2, choices=Permission.choices, default=Permission.WR)

    objects = StoryPublicationManager()

    def __str__(self):
        return self.title + " " + str(self.id)


class StoryChapter(models.Model):
    """Story chapter (continuations of other stories) """

    # story principal a la que hace referencia el capitulo (for get title, image, etc)
    mainStory = models.ForeignKey(StoryPublication, on_delete=models.PROTECT)
    # datos usuario
    own_user = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    # contenido
    text_content = models.TextField(max_length=2000)
    active = models.BooleanField(default=True)  # si es una publicacion activa o no.
    date_time = models.DateField(auto_now_add=True)
    views = models.IntegerField(default=0)  # cantidad de visitas
    valoration = models.IntegerField(default=0)
    tag = models.ManyToManyField("Tag")
    prevChapter = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.PROTECT
    )  # capitulo anterior.
    # responde a pregunta
    quest_answ = models.CharField(max_length=100, null=False)
    like = models.ManyToManyField(
        UserProfile, through="ChapterLike", related_name="chapterLikes", symmetrical=False
    )

    objects = ChapterManager()

    def __str__(self):
        return self.mainStory.title + " - " + str(self.quest_answ)


class StoryLike(models.Model):
    date_time = models.DateField(auto_now_add=True)
    from_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="likeToStory")
    to_story = models.ForeignKey(
        StoryPublication, on_delete=models.CASCADE, related_name="storyLikedBy"
    )


class ChapterLike(models.Model):
    date_time = models.DateField(auto_now_add=True)
    from_user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="likeToChapter"
    )
    to_chapter = models.ForeignKey(
        StoryChapter, on_delete=models.CASCADE, related_name="chapterLikedBy"
    )


'''RESOURCES ARE NOT YET IMPLEMENTED'''


class ResourcePublication(models.Model):
    # datos usuario
    own_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=45)
    user_lastname = models.CharField(max_length=45)
    # contenido
    text_content = models.TextField()
    title = models.CharField(max_length=500, default="a Title")
    img_content_link = models.CharField(max_length=500)
    privacity = models.IntegerField(default=0)  # privado=1 o publico=0
    active = models.BooleanField(default=True)  # si es una publicacion activa o no.
    date_time = models.DateField(auto_now_add=True)
    views = models.IntegerField(default=0)  # cantidad de visitas
    tag = models.ManyToManyField("Tag")
    valoration = models.IntegerField(default=0)

    def __str__(self):
        return self.title + " " + str(self.id)


# Tags
class Tag(models.Model):
    tag = models.CharField(max_length=80)
    creation_date_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.tag
