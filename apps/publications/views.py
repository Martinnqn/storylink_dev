from django.views import generic, View
from django.views.generic.edit import FormMixin
from django.urls import reverse, reverse_lazy
from apps.publications.models import StoryPublication, StoryChapter, ResourcePublication, Tag
from apps.users.models import CustomUser
from apps.users.views import ListUserDataMenuPerfil
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

from django.core.files.storage import FileSystemStorage

default_img = 'gallery/no-img.png'

#listar las publicaciones creadas por un usuario
class ListUserStories(ListUserDataMenuPerfil):
    template_name = 'publications/story/story_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ListUserStories, self).get_context_data(**kwargs)
        user = get_object_or_404(CustomUser, username=self.kwargs.get('username'))
        publications = StoryPublication.objects.filter(own_user = user, active=True)
        conts = []
        for x in publications:
            ds = {}
            if (x.continuatedBy.all().exists()):
                ds.update({'quest_answ': x.continuatedBy.all()[0].quest_answ})
            ds.update({'own_user': x.own_user})
            ds.update({'title': x.title})
            ds.update({'id': x.id})
            ds.update({'active': x.active})
            ds.update({'valoration': x.valoration})
            ds.update({'views': x.views})
            ds.update({'text_content': x.text_content})
            isFirst = not(x.continuatedBy.all().exists())
            if (isFirst):
                    ds.update({'img_content_link': x.img_content_link.url})
            else:
                ds.update({'first_story': x.first_story})
                if (x.first_story is None):
                    ds.update({'img_content_link': x.img_content_link})
                else:
                    firstPub = get_object_or_404(StoryPublication, id=x.first_story)
                    ds.update({'img_content_link': firstPub.img_content_link.url})
            ds.update({'tag': x.tag})
            conts.append(ds)
        context.update({'list_pub': conts})

        return context

#retornar las continuaciones de una story
class StoryContinuations(LoginRequiredMixin, generic.ListView):
    model = StoryChapter
    template_name = 'publications/story/story_list_previews.html'

    def get_queryset(self):
        qs = self.model.objects.filter(mainStory=self.kwargs["pk"], prevChapter__isnull = True)
        return qs

class ChapterContinuations(LoginRequiredMixin, generic.ListView):
    model = StoryChapter
    template_name = 'publications/story/story_list_previews.html'

    def get_queryset(self):
        qs = self.model.objects.filter(prevChapter = self.kwargs["pk"])
        return qs
     

#retornar las pre-stories de una story.
'''class StoryPrevious(LoginRequiredMixin, generic.DetailView):
    model = StoryPublication
    template_name = 'publications/story/story_list_previews.html'

    def get_query_set(self):
        obj = self.get_object() #obtiene el object StoryPublication automaticamente por el pk de la url.
        return obj.continuatedBy.all()

    def get_context_data(self, **kwargs):
        if (self.request.is_ajax()):
            context = super(StoryPrevious, self).get_context_data(**kwargs)
            conts = []
            if (self.get_query_set().exists()):
                x = self.get_query_set()[0];
                ds = {}
                ds.update({'own_user': x.baseStory.own_user})
                ds.update({'title': x.baseStory.title})
                if (x.baseStory.continuationFrom.all().exists()):
                    ds.update({'answer': x.baseStory.continuationFrom.all()[0].quest_answ})
                ds.update({'id': x.baseStory.id})
                ds.update({'active': x.baseStory.active})
                if (x.baseStory.active):
                    ds.update({'valoration': x.baseStory.valoration})
                    ds.update({'views': x.baseStory.views})
                    ds.update({'text_content': x.baseStory.text_content})
                    ds.update({'img_content_link': x.baseStory.img_content_link.url})
                else:
                    ds.update({'text_content': "No se puede visualizar el contenido de esta Storylink."})
                    ds.update({'img_content_link': default_img})
                conts.append(ds)
            context.update({'list_pub': conts})
            return context
        else:
            context = super(StoryPrevious, self).get_context_data(**kwargs)
            return context'''

class StoryPrevious(LoginRequiredMixin, generic.DetailView):
    model = StoryPublication
    template_name = 'publications/story/story_list_previews.html'

    def get_query_set(self):
        obj = self.get_object() #obtiene el object StoryPublication automaticamente por el pk de la url.
        return obj.continuatedBy.all()

    def get(self, *args, **kwargs):
        if (self.request.is_ajax()):
            if (self.get_query_set().exists()):
                publication = self.get_query_set()[0].baseStory
                data =  dict()
                if (publication.active):
                    data['content_pub'] = model_to_dict(publication, exclude=['tag', 'storyContinuation', 'own_user, img_content_link'])
                    data['content_pub'].update({'own_username': publication.own_user.username})
                    data['content_pub'].update({'user_name': publication.own_user.first_name})
                    data['content_pub'].update({'user_lastname': publication.own_user.last_name})
                    data['content_pub'].update({'own_user': publication.own_user.id})
                    data['content_pub'].update({'img_content_link': publication.img_content_link.url})
                    data['content_pub'].update({'first_story': publication.first_story})

                    isFirst = not(publication.continuatedBy.all().exists())
                    data['content_pub'].update({'is_first': isFirst})
                    if (isFirst):
                        data['content_pub'].update({'img_content_link': publication.img_content_link.url})
                    else:
                        data['content_pub'].update({'first_story': publication.first_story})
                        if (publication.first_story is None):
                            data['content_pub'].update({'img_content_link': publication.img_content_link.url})
                        else:
                            firstPub = get_object_or_404(StoryPublication, id=publication.first_story)
                            data['content_pub'].update({'img_content_link': firstPub.img_content_link.url})

                    tags = []
                    for x in publication.tag.all():
                        tags.append(x.tag)
                    data['content_pub'].update({'tags': tags})
                    fromUser = self.request.user
                    is_subscribed = fromUser.user2Pub.filter(pub = publication).exists();
                    data['content_pub'].update({'is_subscribed': is_subscribed})
                else:
                    data['content_pub'] = model_to_dict(publication, exclude=['tag', 'storyContinuation', 
                        'own_user', 'text_content', 'img_content_link'])
                    data['content_pub'].update({'own_username': publication.own_user.username})
                    data['content_pub'].update({'user_name': publication.own_user.first_name})
                    data['content_pub'].update({'user_lastname': publication.own_user.last_name})
                    data['content_pub'].update({'own_user': publication.own_user.id})
                    data['content_pub'].update({'tags': []})
                    data['content_pub'].update({'text_content': "No se puede visualizar el contenido de esta Storylink."})
                    data['content_pub'].update({'img_content_link': default_img})
                return JsonResponse(data)
            else:
                return super().get(*args, **kwargs)
        else:
            return super().get(*args, **kwargs)


#listar el contenido de una story. si es por ajax retorna un json, sino retorna el template correspondiente.
class ListContentStory(LoginRequiredMixin, generic.DetailView):
    model = StoryPublication
    template_name = 'publications/story/story_display.html'
    slug_field = 'username'
    slug_url_kwarg = 'username' 

    def get(self, *args, **kwargs):
        if (self.request.is_ajax()):
            publication = self.get_object()
            data =  dict()
            data['content_pub'] = model_to_dict(publication, exclude=['tag', 'own_user', 'img_content_link'])
            data['content_pub'].update({'own_username': publication.own_user.username})
            data['content_pub'].update({'user_name': publication.own_user.first_name})
            data['content_pub'].update({'user_lastname': publication.own_user.last_name})
            data['content_pub'].update({'own_user': publication.own_user.id})

            if (publication.active):
                tags = []
                for x in publication.tag.all():
                    tags.append(x.tag)
                data['content_pub'].update({'tags': tags})
                data['content_pub'].update({'img_content_link': publication.img_content_link.url})
                fromUser = self.request.user
                is_subscribed = fromUser.user2Pub.filter(pub = publication).exists();
                data['content_pub'].update({'is_subscribed': is_subscribed})
            else:
                data['content_pub'].update({'tags': []})
                data['content_pub'].update({'text_content': "No se puede visualizar el contenido de esta Storylink."})
                data['content_pub'].update({'img_content_link': default_img})
            return JsonResponse(data)
        else:
            return super().get(*args, **kwargs)

class ListContentChapter(LoginRequiredMixin, generic.ListView):
    model = StoryChapter
    template_name = 'publications/story/story_display.html'

    def get(self, *args, **kwargs):
        if (self.request.is_ajax()):
            publication = get_object_or_404(StoryChapter, id=self.kwargs.get('pk'))
            data =  dict()
            data['content_pub'] = model_to_dict(publication, exclude=['tag', 'own_user'])
            data['content_pub'].update({'own_username': publication.own_user.username})
            data['content_pub'].update({'user_name': publication.own_user.first_name})
            data['content_pub'].update({'user_lastname': publication.own_user.last_name})
            data['content_pub'].update({'own_user': publication.own_user.id})
            data['content_pub'].update({'title': publication.mainStory.title})
            data['content_pub'].update({'img_content_link': publication.mainStory.img_content_link.url})

            if (publication.active):
                tags = []
                for x in publication.tag.all():
                    tags.append(x.tag)
                data['content_pub'].update({'tags': tags})
                fromUser = self.request.user
            else:
                data['content_pub'].update({'tags': []})
                data['content_pub'].update({'text_content': "No se puede visualizar el contenido de esta Storylink."})
            return JsonResponse(data)
        else:
            return super().get(*args, **kwargs)


#Eliminar story. No se eliminan, se ponen inactivas
class DeleteStory(LoginRequiredMixin, generic.edit.DeleteView):
    def get(self, request, username, id):
        fromUser = request.user
        story = StoryPublication.objects.get(id=id)
        if (story.own_user == fromUser):
            story.active=False
            story.save(update_fields=['active'])
            if (request.GET.get('next')):
                red = request.GET.get('next')
            else:
                red = reverse_lazy('user:user_profile', kwargs={'username': username})
        else:
            red = reverse_lazy('user:user_profile', kwargs={'username': username})
        return redirect(red)

#Eliminar chapter. No se eliminan, se ponen inactivos
class DeleteChapter(LoginRequiredMixin, generic.edit.DeleteView):
    def get(self, request, username, id):
        story = StoryChapter.objects.get(id=id)
        if (story.own_user == self.request.user):
            story.active=False
            story.save(update_fields=['active'])
            if (request.GET.get('next')):
                red = request.GET.get('next')
            else:
                red = reverse_lazy('user:user_profile', kwargs={'username': username})
        else:
            red = reverse_lazy('user:user_profile', kwargs={'username': username})
        return redirect(red)


#Editar story.
class EditStory(ListUserDataMenuPerfil, generic.edit.UpdateView):
    model = StoryPublication
    form_class = StoryEditForm
    template_name = 'publications/story/edit_story.html'

    def get_success_url(self):
        username=self.kwargs['username']
        return reverse_lazy('user:user_profile', kwargs={'username': username})

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

class EditStoryChapter(ListUserDataMenuPerfil, generic.edit.UpdateView):
    model = StoryChapter
    form_class = StoryChapterEditForm
    template_name = 'publications/story/edit_story.html'

    def get_success_url(self):
        username=self.kwargs['username']
        return reverse_lazy('user:user_profile', kwargs={'username': username})

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
class CreateStory(ListUserDataMenuPerfil, generic.CreateView):
    form_class = StoryCreationForm
    template_name = 'publications/story/create_story.html'

    def form_valid(self, form):
        story = form.save(commit=False)
        story.own_user = self.request.user
        form.save()
        addTags(form.cleaned_data.get('tag').split(), story)

        return redirect(reverse_lazy('user:user_profile', kwargs={'username': self.request.user.username}))

#para dar de alta una continuacion de una Story  
class CreateStoryContinuation(ListUserDataMenuPerfil, generic.CreateView):
    model = StoryPublication
    form_class = StoryContinuationCreationForm
    template_name = 'publications/story/create_story_continuation.html'

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
    def get(self, request, username, id):
        fromUser = self.request.user
        toStory = StoryPublication.objects.get(id=id)
        fromUser.pub_subscription.add(toStory);
        data = dict()
        data.update({'is_subscribed': True})
        data.update({'username': username})
        data.update({'story_id': id})
        return JsonResponse(data)

#remover suscripcion de user a story.
class UnsubscribeStory(LoginRequiredMixin, generic.edit.DeleteView):
    def get(self, request, username, id):
        fromUser = self.request.user
        toStory = StoryPublication.objects.get(id=id)
        fromUser.pub_subscription.remove(toStory);
        data = dict()
        data.update({'is_subscribed': False})
        data.update({'username': username})
        data.update({'story_id': id})
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
class ListUserResources(ListUserDataMenuPerfil):
    template_name = 'publications/resource/resource_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ListUserResources, self).get_context_data(**kwargs)
        user = get_object_or_404(CustomUser, username=self.kwargs.get('username'))
        resources = ResourcePublication.objects.filter(own_user = user, active=True)
        context.update({'list_res': resources})
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
class EditResource(ListUserDataMenuPerfil, generic.edit.UpdateView):
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
class CreateResource(ListUserDataMenuPerfil, generic.CreateView):
    form_class = ResourceCreationForm
    template_name = 'publications/resource/create_resource.html'

    def form_valid(self, form):
        res = form.save(commit=False)
        res.own_user = self.request.user
        res.user_name = self.request.user.first_name
        res.user_lastname = self.request.user.last_name
        form.save()
        return redirect(reverse_lazy('user:pub:user_resources_own', kwargs={'username': self.request.user.username}))
