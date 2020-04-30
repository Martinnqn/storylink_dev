from django.db import models

from apps.users.models import CustomUser


# publicacion tipo historia
class StoryPublication(models.Model):
    #datos usuario
    own_user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    #contenido
    title = models.CharField(max_length=120)
    text_content = models.TextField(max_length=2000)
    #img_content_link = models.URLField(max_length=500)
    img_content_link = models.ImageField(upload_to = 'gallery/publications/', default = 'gallery/no-img.png')
    opened = models.BooleanField(default=True) # privado=False o publico=True
    active = models.BooleanField(default=True) # si es una publicacion activa o no.
    date_time = models.DateField(auto_now_add=True)
    views = models.IntegerField(default=0) #cantidad de visitas
    valoration = models.IntegerField(default=0)
    tag = models.ManyToManyField('Tag')
    color = models.CharField(max_length=7, default="#4a4a4a")
    def __str__(self):
        return self.title+' '+str(self.id)

#capitulos
class StoryChapter(models.Model):
    #story principal a la que hace referencia el capitulo (para obtener el titulo, imagen, etc)
    mainStory = models.ForeignKey(StoryPublication, on_delete=models.PROTECT)
    #datos usuario
    own_user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    #contenido
    text_content = models.TextField(max_length=2000)
    active = models.BooleanField(default=True) # si es una publicacion activa o no.
    date_time = models.DateField(auto_now_add=True)
    views = models.IntegerField(default=0) #cantidad de visitas
    valoration = models.IntegerField(default=0)
    tag = models.ManyToManyField('Tag')
    prevChapter = models.ForeignKey('self', null=True, blank=True, on_delete=models.PROTECT) #capitulo anterior.
    #responde a pregunta
    quest_answ = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.mainStory.title+' - '+str(self.quest_answ)



# publicacion tipo recurso
class ResourcePublication(models.Model):
    #datos usuario
    own_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=45)
    user_lastname = models.CharField(max_length=45)
    #contenido
    text_content = models.TextField()
    title = models.CharField(max_length=500, default='a Title')
    img_content_link = models.CharField(max_length=500)
    privacity = models.IntegerField(default=0) # privado=1 o publico=0
    active = models.BooleanField(default=True) # si es una publicacion activa o no.
    date_time = models.DateField(auto_now_add=True)
    views = models.IntegerField(default=0) #cantidad de visitas
    tag  = models.ManyToManyField('Tag')
    valoration = models.IntegerField(default=0)

    def __str__(self):
        return self.title+' '+str(self.id)

# Tags
class Tag(models.Model):
    tag = models.CharField(max_length=80)
    creation_date_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.tag