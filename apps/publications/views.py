from django.views import generic, View
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from apps.publications.models import StoryPublication, StoryChapter, ResourcePublication, Tag, Permission
from apps.users.models import CustomUser
from apps.users.views import ListUserPerfil
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.publications.forms import StoryCreationForm, StoryContinuationCreationForm, StoryEditForm, StoryChapterEditForm
from apps.publications.forms import ResourceEditForm, ResourceCreationForm
from apps.publications.forms import FilterHall
from django.http import JsonResponse, Http404
from django.forms.models import model_to_dict
from django.db import transaction, IntegrityError
from django.conf import settings

default_img = settings.MEDIA_URL+'/gallery/no-img.png'

#listar las Stories creadas por un usuario
class ListUserStories(LoginRequiredMixin, generic.ListView):
    models = StoryPublication
    template_name = 'publications/story/publications_user.html'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(CustomUser, username=self.kwargs["username"])
        qs = StoryPublication.objects.get_stories_by_user(user, self.request.user).order_by('date_time__month', '-date_time__day')
        return qs.order_by('date_time__month', '-date_time__day')

    def get_context_data(self, **kwargs):
        context = super(ListUserStories, self).get_context_data(**kwargs)
        context.update({'customuser': {'username':self.kwargs["username"]}})
        return context

#retornar las continuaciones de una story
class StoryContinuations(LoginRequiredMixin, generic.ListView):
    model = StoryChapter
    template_name = 'publications/story/list_chapters_preview.html'

    def get_queryset(self):
        qs = self.model.objects.story_continuations(self.kwargs["pk"], self.request.user)
        return qs

#retornar las continuaciones de un chapter
class ChapterContinuations(LoginRequiredMixin, generic.ListView):
    model = StoryChapter
    template_name = 'publications/story/list_chapters_preview.html'

    def get_queryset(self):
        qs = self.model.objects.chapter_continuations(self.kwargs["pk"], self.request.user)
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
        publication = self.get_object()
        own_user = publication.own_user
        if (self.request.is_ajax()):
            data =  dict()
            if (not publication.status==Permission.NR or own_user==self.request.user.profile.get()):
                data['content_pub'] = model_to_dict(publication, exclude=['id', 'tag', 'own_user', 'img_content_link', 'like'])
                data['content_pub'].update({'id': 'story_'+str(publication.id)})
                data['content_pub'].update({'own_username': own_user.user.username})
                data['content_pub'].update({'user_name': own_user.user.first_name})
                data['content_pub'].update({'user_lastname': own_user.user.last_name})
                data['content_pub'].update({'own_user': own_user.id})
                data['content_pub'].update({'own_first_story': own_user.id})
                data['content_pub'].update({'url_delete': reverse_lazy('user:pub:delete_story', kwargs={'username': own_user.user.username, 'pk': publication.id})})
                data['content_pub'].update({'url_edit': reverse_lazy('user:pub:edit_story', kwargs={'username': own_user.user.username, 'pk': publication.id})})
                data['content_pub'].update({'url_subscribe': reverse_lazy('user:pub:subs_story', kwargs={'username': own_user.user.username, 'pk': publication.id})})
                data['content_pub'].update({'url_unsubscribe': reverse_lazy('user:pub:unsubs_story', kwargs={'username': own_user.user.username, 'pk': publication.id})})
                data['content_pub'].update({'url_like': reverse_lazy('user:pub:like_story', kwargs={'username': own_user.user.username, 'pk': publication.id})})
                data['content_pub'].update({'url_unlike': reverse_lazy('user:pub:unlike_story', kwargs={'username': own_user.user.username, 'pk': publication.id})})
                data['content_pub'].update({'url_continuate': reverse_lazy('user:pub:create_story_cont', kwargs={'username': own_user.user.username, 'pk': publication.id})})
                data['content_pub'].update({'url_continuations': reverse_lazy('user:pub:conts_story', kwargs={'username': own_user.user.username, 'pk': publication.id})})
                data['content_pub'].update({'url_autor': reverse_lazy('user:user_profile', kwargs={'username': own_user.user.username})})
                data['content_pub'].update({'active': publication.active})
                data['content_pub'].update({'color': publication.color})
                opened = (publication.status==Permission.WR)
                data['content_pub'].update({'opened': opened})
                
                fromUser = self.request.user
                is_liked = fromUser.profile.get().likeToStory.filter(to_story = publication).exists();
                data['content_pub'].update({'is_liked': is_liked})
                
                cantLikes = publication.like.count();
                data['content_pub'].update({'cant_likes': cantLikes})

                profile = own_user
                data['content_pub'].update({'own_user_image': profile.link_img_perfil.url})

                if (publication.active):
                    tags = []
                    for x in publication.tag.all():
                        tags.append(x.tag)
                    data['content_pub'].update({'tags': tags})
                    data['content_pub'].update({'img_content_link': publication.img_content_link.url})
                    is_subscribed = fromUser.profile.get().user2Pub.filter(pub = publication).exists();
                    data['content_pub'].update({'is_subscribed': is_subscribed})
                else:
                    data['content_pub'].update({'tags': []})
                    data['content_pub'].update({'text_content': "No se puede visualizar el contenido de esta Storylink."})
                    data['content_pub'].update({'img_content_link': default_img})
            return JsonResponse(data)
        else:
            if (not publication.status==Permission.NR or own_user==self.request.user.profile.get()):
                return super().get(*args, **kwargs)
            raise Http404()

#listar el contenido de un capitulo
class ListContentChapter(LoginRequiredMixin, generic.DetailView):
    model = StoryChapter
    template_name = 'publications/story/story_display.html'

    def get_context_data(self, **kwargs):
        context = super(ListContentChapter, self).get_context_data(**kwargs)
        context.update({'customuser': {'username':self.kwargs["username"]}})
        return context
        
    def get(self, *args, **kwargs):
        publication = self.get_object()
        own_user = publication.own_user
        mainStory = publication.mainStory
        if (self.request.is_ajax()):
            data =  dict()
            if (not mainStory.status==Permission.NR or own_user==self.request.user.profile.get()):
                data['content_pub'] = model_to_dict(publication, exclude=['id', 'tag', 'own_user', 'like'])
                data['content_pub'].update({'id': 'chapter_'+str(publication.id)})
                data['content_pub'].update({'own_username': own_user.user.username})
                data['content_pub'].update({'user_name': own_user.user.first_name})
                data['content_pub'].update({'user_lastname': own_user.user.last_name})
                data['content_pub'].update({'own_user': own_user.id})
                data['content_pub'].update({'title': mainStory.title})
                data['content_pub'].update({'own_first_story': mainStory.own_user.id})
                data['content_pub'].update({'own_name_first_story': mainStory.own_user.user.username})
                data['content_pub'].update({'question': publication.quest_answ})
                data['content_pub'].update({'url_delete': reverse_lazy('user:pub:delete_chapt', kwargs={'username': own_user.user.username, 'pk': publication.id})})
                data['content_pub'].update({'url_edit': reverse_lazy('user:pub:edit_chapter', kwargs={'username': own_user.user.username, 'pk': publication.id})})
                data['content_pub'].update({'url_subscribe': reverse_lazy('user:pub:subs_story', kwargs={'username': own_user.user.username, 'pk': mainStory.id})})
                data['content_pub'].update({'url_unsubscribe': reverse_lazy('user:pub:unsubs_story', kwargs={'username': own_user.user.username, 'pk': mainStory.id})})
                data['content_pub'].update({'url_like': reverse_lazy('user:pub:like_chapter', kwargs={'username': own_user.user.username, 'pk': publication.id})})
                data['content_pub'].update({'url_unlike': reverse_lazy('user:pub:unlike_chapter', kwargs={'username': own_user.user.username, 'pk': publication.id})})
                data['content_pub'].update({'url_continuate': reverse_lazy('user:pub:create_story_cont', kwargs={'username': own_user.user.username, 'pk': mainStory.id, 'pkchapter': publication.id})})
                data['content_pub'].update({'url_continuations': reverse_lazy('user:pub:conts_chap', kwargs={'username': own_user.user.username, 'pk': publication.id})})
                data['content_pub'].update({'url_first_story': reverse_lazy('user:pub:story_content', kwargs={'username': own_user.user.username, 'pk': mainStory.id})})
                data['content_pub'].update({'url_autor': reverse_lazy('user:user_profile', kwargs={'username': own_user.user.username})})
                data['content_pub'].update({'url_autor_init': reverse_lazy('user:user_profile', kwargs={'username': mainStory.own_user.user.username})})
                data['content_pub'].update({'color': mainStory.color})
                data['content_pub'].update({'id_main_story': mainStory.id})
                opened = (mainStory.status==Permission.WR)
                data['content_pub'].update({'opened': opened})
                fromUser = self.request.user
                is_subscribed = fromUser.profile.get().user2Pub.filter(pub = mainStory).exists();
                data['content_pub'].update({'is_subscribed': is_subscribed})
                
                is_liked = fromUser.profile.get().likeToChapter.filter(to_chapter = publication).exists();
                data['content_pub'].update({'is_liked': is_liked})
                
                cantLikes = publication.like.count();
                data['content_pub'].update({'cant_likes': cantLikes})

                profile = own_user
                data['content_pub'].update({'own_user_image': profile.link_img_perfil.url})

                prev =publication.prevChapter
                if (prev):
                    data['content_pub'].update({'previous_pub_id': 'chapter_'+str(prev.id)})
                    data['content_pub'].update({'url_prev_chapter': reverse_lazy('user:pub:chapter_content', kwargs={'username': own_user.user.username, 'pk': publication.prevChapter.id})})
                else:
                    data['content_pub'].update({'previous_pub_id': 'story_'+str(mainStory.id)})
                    data['content_pub'].update({'url_prev_chapter': None})

                data['content_pub'].update({'active': publication.active})

                if (publication.active):
                    tags = []
                    for x in publication.tag.all():
                        tags.append(x.tag)
                    data['content_pub'].update({'tags': tags})
                    data['content_pub'].update({'img_content_link': mainStory.img_content_link.url})
                else:
                    data['content_pub'].update({'tags': []})
                    data['content_pub'].update({'text_content': "No se puede visualizar el contenido de esta Storylink."})
                    data['content_pub'].update({'img_content_link': default_img})
            return JsonResponse(data)
        else:
            if (not mainStory.status==Permission.NR or own_user==self.request.user.profile.get()):
                return super().get(*args, **kwargs)
            raise Http404()


#Eliminar story. No se eliminan, se ponen inactivas
class DeleteStory(LoginRequiredMixin, generic.edit.DeleteView):
    def get(self, request, username, pk):
        fromUser = request.user.profile.get()
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

    def get(self,  *args, **kwargs):
        story = self.get_object()
        if (story.own_user != self.request.user.profile.get()):
            return redirect(reverse_lazy('user:user_profile', kwargs={'username': self.request.user.username}))
        else:
            return super().get(*args, **kwargs)

    def form_valid(self, form):
        story = self.get_object()
        if (story.own_user == self.request.user.profile.get()):
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

    def get(self, *args, **kwargs):
        chap = self.get_object()
        if (chap.own_user != self.request.user.profile.get()):
            return redirect(reverse_lazy('user:user_profile', kwargs={'username': self.request.user.username}))
        else:
            return super().get(*args, **kwargs)

    def form_valid(self, form):
        chap = self.get_object()
        if (chap.own_user == self.request.user.profile.get()):
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
        try:
            with transaction.atomic():
                story = form.save(commit=False)
                story.own_user = self.request.user.profile.get()
                form.save()
        except IntegrityError as e:
            print("Errorrrrr "+e.message)
        addTags(form.cleaned_data.get('tag').split(), story)
        return redirect(reverse_lazy('user:user_profile', kwargs={'username': self.request.user.username}))

    def form_invalid(self, form):
        context = dict()
        context.update({'customuser': {'username':self.kwargs["username"]}})
        context.update({'form':form});
        return render(self.request, 'publications/story/create_story.html', context)

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
        storyMain = get_object_or_404(StoryPublication, id = self.kwargs.get('pk'))
        if (storyMain.status==Permission.WR or (self.request.user.profile.get() == storyMain.own_user)):
            try:
                with transaction.atomic():
                    story = form.save(commit=False)
                    story.own_user = self.request.user.profile.get()
                    #if (form.cleaned_data.get("previous_story_id") != None):
                    #base_pub = get_object_or_404(StoryPublication, id = form.cleaned_data.get("previous_story_id"))
                    if (storyMain):
                        story.mainStory=storyMain

                    if (self.kwargs.get('pkchapter')):
                        prevChap = get_object_or_404(StoryChapter, id = self.kwargs.get('pkchapter'))
                        story.prevChapter=prevChap
                    form.save()
            except IntegrityError as e:
                    print("Errorrrrr "+e.message)
            addTags(form.cleaned_data.get('tag').split(), story)
        return redirect(reverse_lazy('user:user_profile', kwargs={'username': self.request.user.username}))
    
    #si status es WR o el usuario que la modifica es el duenio entonces se procede normalmente, sino se redirige al hall.
    def get(self, *args, **kwargs):
        fromUser = self.request.user
        storyMain = get_object_or_404(StoryPublication, id = self.kwargs.get('pk'))
        if (storyMain.status==Permission.WR or (fromUser.profile.get() == storyMain.own_user)):
            return super().get(*args, **kwargs)
        return redirect(reverse_lazy('hall'))

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
class SubscribeStory(LoginRequiredMixin, View):
    def get(self, request, username, pk):
        fromUser = self.request.user.profile.get()
        toStory = get_object_or_404(StoryPublication, id = pk)
        fromUser.pub_subscription.add(toStory);
        data = dict()
        data.update({'is_subscribed': True})
        data.update({'story_id': pk})
        return JsonResponse(data)

#remover suscripcion de user a story.
class UnsubscribeStory(LoginRequiredMixin, View):
    def get(self, request, username, pk):
        fromUser = self.request.user.profile.get()
        toStory = get_object_or_404(StoryPublication, id = pk)
        fromUser.pub_subscription.remove(toStory);
        data = dict()
        data.update({'is_subscribed': False})
        data.update({'story_id': pk})
        return JsonResponse(data)

#agregar like de user a story.
class LikeStory(LoginRequiredMixin, View):
    def get(self, request, username, pk):
        fromUser = self.request.user.profile.get()
        toStory = get_object_or_404(StoryPublication, id = pk)
        toStory.like.add(fromUser);
        data = dict()
        data.update({'is_liked': True})
        data.update({'story_id': pk})
        return JsonResponse(data)

#remover like de user a story.
class UnlikeStory(LoginRequiredMixin, View):
    def get(self, request, username, pk):
        fromUser = self.request.user.profile.get()
        toStory = get_object_or_404(StoryPublication, id = pk)
        toStory.like.remove(fromUser);
        data = dict()
        data.update({'is_liked': False})
        data.update({'story_id': pk})
        return JsonResponse(data)

#agregar like de user a chapter.
class LikeChapter(LoginRequiredMixin, View):
    def get(self, request, username, pk):
        fromUser = self.request.user.profile.get()
        toChapter = get_object_or_404(StoryChapter, id = pk)
        toChapter.like.add(fromUser);
        data = dict()
        data.update({'is_liked': True})
        data.update({'story_id': pk})
        return JsonResponse(data)

#remover like de user a chapter.
class UnlikeChapter(LoginRequiredMixin, View):
    def get(self, request, username, pk):
        fromUser = self.request.user.profile.get()
        toChapter = get_object_or_404(StoryChapter, id = pk)
        toChapter.like.remove(fromUser);
        data = dict()
        data.update({'is_liked': False})
        data.update({'story_id': pk})
        return JsonResponse(data)

#HALL
class ListStories(LoginRequiredMixin, FormMixin, generic.ListView):
    model = StoryPublication
    template_name = 'hall/hall.html'
    form_class = FilterHall
    paginate_by = 30

    def get_queryset(self):
        qs = StoryPublication.objects.publications_hall(self.request.GET.get('title',None),
         self.request.GET.get('tag', None))
        return qs

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)
        self.request = request
        # From BaseListView
        self.object_list = self.get_queryset()
        context = self.get_context_data(object_list=self.object_list, form=self.form)
        context.update({'activated': self.kwargs.get('activated',None)})
        return self.render_to_response(context)


#API DESDE ACA

class StoryContinuationsTitle(LoginRequiredMixin, FormMixin, generic.ListView):
    model = StoryPublication
    
    def get(self, *args, **kwargs):
        if (self.request.is_ajax()):
            data = { 'childs': [{'pubId': "1", 'title': 'Story1'},
             {'pubId': "2", 'title': 'Story2'}, {'pubId': "3", 'title': 'Story3'}]}
            return JsonResponse(data)
        else:
            raise Http404()
            
        
class ChapterContinuationsTitle(LoginRequiredMixin, FormMixin, generic.ListView):
    model = StoryPublication
    
    def get(self, *args, **kwargs):
        if (self.request.is_ajax()):
            data = data = { 'childs': [{'pubId': "1", 'title': 'ssStory1'},
             {'pubId': "2", 'title': 'ssStory2'}, {'pubId': "3", 'title': 'ssStory3'}]}
            return JsonResponse(data)
        else:
            raise Http404()
            
        