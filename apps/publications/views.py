from django.views import generic, View
from django.views.generic.edit import FormMixin
from django.urls import reverse, reverse_lazy
from apps.publications.models import StoryPublication, StoryChapter, ResourcePublication, Tag
from apps.users.models import CustomUser
from apps.users.views import ListUserPerfil
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.publications.forms import StoryCreationForm, StoryContinuationCreationForm, StoryEditForm, StoryChapterEditForm
from apps.publications.forms import ResourceEditForm, ResourceCreationForm
from apps.publications.forms import FilterHall
from django.http import JsonResponse, Http404, HttpResponseForbidden
from django.forms.models import model_to_dict
from django.db import transaction, IntegrityError
from django.db.models import Q
from django.db.models import Count
from django.conf import settings

from django.core.files.storage import FileSystemStorage

default_img = settings.MEDIA_URL+'/gallery/no-img.png'

#listar las Stories creadas por un usuario
class ListUserStories(LoginRequiredMixin, generic.ListView):
    models = StoryPublication
    template_name = 'publications/story/publications_user.html'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(CustomUser, username=self.kwargs["username"])
        qs = StoryPublication.objects.filter(own_user=user)
        return qs

    def get_context_data(self, **kwargs):
        context = super(ListUserStories, self).get_context_data(**kwargs)
        context.update({'customuser': {'username':self.kwargs["username"]}})
        return context

#retornar las continuaciones de una story
class StoryContinuations(LoginRequiredMixin, generic.ListView):
    model = StoryChapter
    template_name = 'publications/story/list_chapters_preview.html'

    def get_queryset(self):
        qs = self.model.objects.filter(mainStory=self.kwargs["pk"], prevChapter__isnull = True)
        return qs

#retornar las continuaciones de un chapter
class ChapterContinuations(LoginRequiredMixin, generic.ListView):
    model = StoryChapter
    template_name = 'publications/story/list_chapters_preview.html'

    def get_queryset(self):
        qs = self.model.objects.filter(prevChapter = self.kwargs["pk"])
        return qs


#listar el contenido de una story. si es por ajax retorna un json, sino retorna el template correspondiente.
class ListContentStory(LoginRequiredMixin, generic.DetailView):
    model = StoryPublication
    template_name = 'publications/story/story_display.html'

    def get_context_data(self, **kwargs):
        context = super(ListContentStory, self).get_context_data(**kwargs)
        context.update({'customuser': {'username':self.kwargs["username"]}})
        return context

    def get(self, *args, **kwargs):
        if (self.request.is_ajax()):
            publication = self.get_object()
            own_user = publication.own_user
            data =  dict()
            data['content_pub'] = model_to_dict(publication, exclude=['tag', 'own_user', 'img_content_link'])
            data['content_pub'].update({'own_username': own_user.username})
            data['content_pub'].update({'user_name': own_user.first_name})
            data['content_pub'].update({'user_lastname': own_user.last_name})
            data['content_pub'].update({'own_user': own_user.id})
            data['content_pub'].update({'own_user_image': self.request.build_absolute_uri(own_user.link_img_perfil.url)})
            data['content_pub'].update({'url_delete': reverse_lazy('user:pub:delete_story', kwargs={'username': own_user.username, 'pk': publication.id})})
            data['content_pub'].update({'url_edit': reverse_lazy('user:pub:edit_story', kwargs={'username': own_user.username, 'pk': publication.id})})
            data['content_pub'].update({'url_subscribe': reverse_lazy('user:pub:subs_story', kwargs={'username': own_user.username, 'pk': publication.id})})
            data['content_pub'].update({'url_unsubscribe': reverse_lazy('user:pub:unsubs_story', kwargs={'username': own_user.username, 'pk': publication.id})})
            data['content_pub'].update({'url_continuate': reverse_lazy('user:pub:create_story_cont', kwargs={'username': own_user.username, 'pk': publication.id})})
            data['content_pub'].update({'url_continuations': reverse_lazy('user:pub:conts_story', kwargs={'username': own_user.username, 'pk': publication.id})})
            data['content_pub'].update({'url_autor': reverse_lazy('user:user_profile', kwargs={'username': own_user.username})})
            data['content_pub'].update({'active': publication.active})

            if (publication.active):
                tags = []
                for x in publication.tag.all():
                    tags.append(x.tag)
                data['content_pub'].update({'tags': tags})
                data['content_pub'].update({'img_content_link': self.request.build_absolute_uri(publication.img_content_link.url)})
                fromUser = self.request.user
                is_subscribed = fromUser.user2Pub.filter(pub = publication).exists();
                data['content_pub'].update({'is_subscribed': is_subscribed})
            else:
                data['content_pub'].update({'tags': []})
                data['content_pub'].update({'text_content': "No se puede visualizar el contenido de esta Storylink."})
                data['content_pub'].update({'img_content_link': self.request.build_absolute_uri(default_img)})
            return JsonResponse(data)
        else:
            return super().get(*args, **kwargs)

#listar el contenido de un capitulo
class ListContentChapter(LoginRequiredMixin, generic.DetailView):
    model = StoryChapter
    template_name = 'publications/story/story_display.html'

    def get_context_data(self, **kwargs):
        context = super(ListContentChapter, self).get_context_data(**kwargs)
        context.update({'customuser': {'username':self.kwargs["username"]}})
        return context
        
    def get(self, *args, **kwargs):
        if (self.request.is_ajax()):
            publication = self.get_object()
            own_user = publication.own_user
            mainStory = publication.mainStory
            data =  dict()
            data['content_pub'] = model_to_dict(publication, exclude=['tag', 'own_user'])
            data['content_pub'].update({'own_username': own_user.username})
            data['content_pub'].update({'user_name': own_user.first_name})
            data['content_pub'].update({'user_lastname': own_user.last_name})
            data['content_pub'].update({'own_user': own_user.id})
            data['content_pub'].update({'title': mainStory.title})
            data['content_pub'].update({'own_first_story': mainStory.own_user.id})
            data['content_pub'].update({'question': publication.quest_answ})
            data['content_pub'].update({'own_user_image': self.request.build_absolute_uri(own_user.link_img_perfil.url)})
            data['content_pub'].update({'url_delete': reverse_lazy('user:pub:delete_chapt', kwargs={'username': own_user.username, 'pk': publication.id})})
            data['content_pub'].update({'url_edit': reverse_lazy('user:pub:edit_chapter', kwargs={'username': own_user.username, 'pk': publication.id})})
            data['content_pub'].update({'url_subscribe': reverse_lazy('user:pub:subs_story', kwargs={'username': own_user.username, 'pk': mainStory.id})})
            data['content_pub'].update({'url_unsubscribe': reverse_lazy('user:pub:unsubs_story', kwargs={'username': own_user.username, 'pk': mainStory.id})})
            data['content_pub'].update({'url_continuate': reverse_lazy('user:pub:create_story_cont', kwargs={'username': own_user.username, 'pk': mainStory.id, 'pkchapter': publication.id})})
            data['content_pub'].update({'url_continuations': reverse_lazy('user:pub:conts_chap', kwargs={'username': own_user.username, 'pk': publication.id})})
            data['content_pub'].update({'url_first_story': reverse_lazy('user:pub:story_content', kwargs={'username': own_user.username, 'pk': mainStory.id})})
            data['content_pub'].update({'url_autor': reverse_lazy('user:user_profile', kwargs={'username': own_user.username})})
            
            prev =publication.prevChapter
            if (prev):
                data['content_pub'].update({'url_prev_chapter': reverse_lazy('user:pub:chapter_content', kwargs={'username': own_user.username, 'pk': publication.prevChapter.id})})
            else:
                data['content_pub'].update({'url_prev_chapter': None})

            data['content_pub'].update({'active': publication.active})

            if (publication.active):
                tags = []
                for x in publication.tag.all():
                    tags.append(x.tag)
                data['content_pub'].update({'tags': tags})
                fromUser = self.request.user
                data['content_pub'].update({'img_content_link': self.request.build_absolute_uri(mainStory.img_content_link.url)})
                fromUser = self.request.user
                is_subscribed = fromUser.user2Pub.filter(pub = mainStory).exists();
                data['content_pub'].update({'is_subscribed': is_subscribed})
            else:
                data['content_pub'].update({'tags': []})
                data['content_pub'].update({'text_content': "No se puede visualizar el contenido de esta Storylink."})
                data['content_pub'].update({'img_content_link': self.request.build_absolute_uri(default_img)})
            return JsonResponse(data)
        else:
            return super().get(*args, **kwargs)


#Eliminar story. No se eliminan, se ponen inactivas
class DeleteStory(LoginRequiredMixin, generic.edit.DeleteView):
    def get(self, request, username, pk):
        fromUser = request.user
        story = StoryPublication.objects.get(id=pk)
        if (story.own_user == fromUser):
            story.active=False
            story.save(update_fields=['active'])
        red = reverse_lazy('user:user_profile', kwargs={'username': username})
        return redirect(red)

#Eliminar chapter. No se eliminan, se ponen inactivos
class DeleteChapter(LoginRequiredMixin, generic.edit.DeleteView):
    def get(self, request, username, pk):
        story = StoryChapter.objects.get(id=pk)
        if (story.own_user == self.request.user):
            story.active=False
            story.save(update_fields=['active'])
        red = reverse_lazy('user:user_profile', kwargs={'username': username})
        return redirect(red)


#Editar story.
class EditStory(LoginRequiredMixin, generic.edit.UpdateView):
    model = StoryPublication
    form_class = StoryEditForm
    template_name = 'publications/story/edit_story.html'

    def get_success_url(self):
        username=self.kwargs['username']
        return reverse_lazy('user:user_profile', kwargs={'username': username})

    def get_context_data(self, **kwargs):
        context = super(EditStory, self).get_context_data(**kwargs)
        context.update({'customuser': {'username':self.kwargs["username"]}})
        return context

    def get(self, *args, username, pk, **kwargs):
        story = self.get_object()
        if (story.own_user != self.request.user):
            return redirect(reverse_lazy('user:user_profile', kwargs={'username': self.request.user.username}))
        else:
            return super().get(*args, **kwargs)

    def form_valid(self, form):
        story = self.get_object()
        if (story.own_user == self.request.user):
            form.save()
            addTags(form.cleaned_data.get('tag').split(), story)
        return redirect(reverse_lazy('user:user_profile', kwargs={'username': self.request.user.username}))

#editar chapter
class EditStoryChapter(LoginRequiredMixin, generic.edit.UpdateView):
    model = StoryChapter
    form_class = StoryChapterEditForm
    template_name = 'publications/story/edit_story.html'

    def get_success_url(self):
        username=self.kwargs['username']
        return reverse_lazy('user:user_profile', kwargs={'username': username})

    def get_context_data(self, **kwargs):
        context = super(EditStoryChapter, self).get_context_data(**kwargs)
        context.update({'customuser': {'username':self.kwargs["username"]}})
        return context



    def get(self, *args, username, pk, **kwargs):
        chap = self.get_object()
        if (chap.own_user != self.request.user):
            return redirect(reverse_lazy('user:user_profile', kwargs={'username': self.request.user.username}))
        else:
            return super().get(*args, **kwargs)

    def form_valid(self, form):
        chap = self.get_object()
        if (chap.own_user == self.request.user):
            form.save()
            addTags(form.cleaned_data.get('tag').split(), chap)
        return redirect(reverse_lazy('user:user_profile', kwargs={'username': self.request.user.username}))


#para dar de alta una Story
class CreateStory(LoginRequiredMixin, generic.CreateView):
    form_class = StoryCreationForm
    template_name = 'publications/story/create_story.html'

    def get_context_data(self, **kwargs):
        context = super(CreateStory, self).get_context_data(**kwargs)
        context.update({'customuser': {'username':self.kwargs["username"]}})
        return context

    def form_valid(self, form):
        story = form.save(commit=False)
        story.own_user = self.request.user
        form.save()
        addTags(form.cleaned_data.get('tag').split(), story)
        return redirect(reverse_lazy('user:user_profile', kwargs={'username': self.request.user.username}))

#para dar de alta un chapter. Esta clase requiere detail y create view. create para obtener
#un formulario correspondiente al StoryContinuationCreationForm, junto con su form_isvalid().
#detailview se requiere para obtener la StoryPublication a la que hace referencia el chapter.
#La storyPublication se obtiene por el pk de la url, y django obtiene la story automaticamente.
class CreateStoryContinuation(LoginRequiredMixin, generic.DetailView, generic.CreateView):
    model = StoryPublication
    form_class = StoryContinuationCreationForm
    template_name = 'publications/story/create_story_continuation.html'

    def get_context_data(self, **kwargs):
        context = super(CreateStoryContinuation, self).get_context_data(**kwargs)
        context.update({'customuser': {'username':self.kwargs["username"]}})
        return context

    def form_valid(self, form):
        story = form.save(commit=False)
        story.own_user = self.request.user
        try:
            with transaction.atomic():
                #if (form.cleaned_data.get("previous_story_id") != None):
                #base_pub = get_object_or_404(StoryPublication, id = form.cleaned_data.get("previous_story_id"))
                mainS = get_object_or_404(StoryPublication, id = self.kwargs.get('pk'))
                if (mainS):
                    story.mainStory=mainS

                if (self.kwargs.get('pkchapter')):
                    prevChap = get_object_or_404(StoryChapter, id = self.kwargs.get('pkchapter'))
                    story.prevChapter=prevChap
                form.save()
        except IntegrityError as e:
                print("Errorrrrr "+e.message)
        addTags(form.cleaned_data.get('tag').split(), story)
        return redirect(reverse_lazy('user:user_profile', kwargs={'username': self.request.user.username}))
    

'''no se agregan tags de manera atomica entre una Story y el Tag. 
Para eso usar el transaction.atomic, aunque no es critico perder tags...'''
#recibe un array de tags. story puede ser story o storychapter
def addTags(tags, story):
    if(story):
        #eliminar los tags que ya no esten en story
        for t in story.tag.all():
            if (t.tag not in tags):
                story.tag.remove(t)
        #agregar los nuevos tags
        for t in tags:
            if (t not in story.tag.all()):
                tag, isCreated = Tag.objects.get_or_create(tag = t)
                story.tag.add(tag)



#agregar suscripcion de user a story.
class SubscribeStory(LoginRequiredMixin, generic.edit.DeleteView):
    def get(self, request, username, pk):
        fromUser = self.request.user
        toStory = get_object_or_404(StoryPublication, id = pk)
        fromUser.pub_subscription.add(toStory);
        data = dict()
        data.update({'is_subscribed': True})
        data.update({'story_id': pk})
        return JsonResponse(data)

#remover suscripcion de user a story.
class UnsubscribeStory(LoginRequiredMixin, generic.edit.DeleteView):
    def get(self, request, username, pk):
        fromUser = self.request.user
        toStory = get_object_or_404(StoryPublication, id = pk)
        fromUser.pub_subscription.remove(toStory);
        data = dict()
        data.update({'is_subscribed': False})
        data.update({'story_id': pk})
        return JsonResponse(data)

#HALL
class ListStories(LoginRequiredMixin, FormMixin, generic.ListView):
    model = StoryPublication
    template_name = 'hall/hall.html'
    form_class = FilterHall
    paginate_by = 30

    '''retorna las publicaciones activas que sean la raiz de las stories, filtradas por el titulo y el tag. 
    Si hay mas de un tag se filtran con un "or", por lo que pueden devolver duplicadas por eso se usa el
    distinct. Se ordenan por cantidad de tags que tenga cada story de manera descendente y por fecha.
    Osea las que tienen igual cantidad de tags se organizan entre si por fecha menos recientes primero'''
    def get_queryset(self):
        qact = Q(active=True)
        qs1 = qact
        qs = StoryPublication.objects.filter(qs1)
        qs2 = Q()
        if ('title' in self.request.GET):
            qs1 &= Q(title__icontains = self.request.GET['title'])
            qs = qs.filter(qs1)
        if ('tag' in self.request.GET):
            for t in self.request.GET['tag'].split():
                qs2 |= Q(tag__tag__icontains = t)
            qs = qs.filter(qs2)
        qs = qs.annotate(count=Count('tag')).order_by('-count', 'date_time')
        return qs.distinct()


    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)
        self.request = request
        # From BaseListView
        self.object_list = self.get_queryset()
        context = self.get_context_data(object_list=self.object_list, form=self.form)
        return self.render_to_response(context)

    '''def post(self, request, *args, **kwargs):
        return self.get(self, request, *args, **kwargs)#no anda porque en get query set pregunta por request.GET'''




#RESOURCES

#listar los resources creados por un usuario
class ListUserResources(LoginRequiredMixin, generic.DetailView):
    template_name = 'publications/resource/resource_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ListUserResources, self).get_context_data(**kwargs)
        context.update({'customuser': {'username':self.kwargs["username"]}})
        return context

#listar el contenido de un resource
class JSONContentResource(LoginRequiredMixin, generic.DetailView):
    def get(self, request, username, pk):
        resource = get_object_or_404(ResourcePublication, id=pk, active=True)
        data =  dict()
        data['content_pub'] = model_to_dict(resource, exclude=['tag'])
        data['content_pub'].update({'own_username': resource.own_user.username})
        data['content_pub'].update({'own_user': resource.own_user.id})
        tags = []
        for x in resource.tag.all():
            tags.append(x.tag)
        data['content_pub'].update({'tags': tags})
        return JsonResponse(data)


#Editar resource.
class EditResource(ListUserPerfil, generic.edit.UpdateView):
    model = ResourcePublication
    form_class = ResourceEditForm
    template_name = 'publications/resource/edit_resource.html'

    def get_query_set(self):
        qs1 = ResourcePublication.objects.filter(active=True, id=self.kwargs.get('pk'))
        return qs1

    def get_success_url(self):
        pubid=self.kwargs['pk']
        username=self.kwargs['username']
        return reverse_lazy('user:pub:user_resources_own', kwargs={'username': username})


#para dar de alta un resource
class CreateResource(ListUserPerfil, generic.CreateView):
    form_class = ResourceCreationForm
    template_name = 'publications/resource/create_resource.html'

    def form_valid(self, form):
        res = form.save(commit=False)
        res.own_user = self.request.user
        res.user_name = self.request.user.first_name
        res.user_lastname = self.request.user.last_name
        form.save()
        return redirect(reverse_lazy('user:pub:user_resources_own', kwargs={'username': self.request.user.username}))
