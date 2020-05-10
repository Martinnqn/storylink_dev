from django.urls import path

from apps.publications.views import *

app_name='pub'

urlpatterns = [
path('story/', ListUserStories.as_view(), name='user_stories_own'),
path('story-content/<int:pk>', ListContentStory.as_view(), name='story_content'),
path('chapter-content/<int:pk>', ListContentChapter.as_view(), name='chapter_content'),
path('create-story', CreateStory.as_view(), name='create_story'),
path('<int:pk>/create-story', CreateStoryContinuation.as_view(), name='create_story_cont'),
path('<int:pk>/<int:pkchapter>/create-story', CreateStoryContinuation.as_view(), name='create_story_cont'),
path('delete-story/<int:pk>', DeleteStory.as_view(), name='delete_story'),
path('delete-chapter/<int:pk>', DeleteChapter.as_view(), name='delete_chapt'),
path('edit-story/<int:pk>', EditStory.as_view(), name='edit_story'),
path('edit-chapter/<int:pk>', EditStoryChapter.as_view(), name='edit_chapter'),
path('subscribe/<int:pk>', SubscribeStory.as_view(), name='subs_story'),
path('unsubscribe/<int:pk>', UnsubscribeStory.as_view(), name='unsubs_story'),
path('story/like/<int:pk>', LikeStory.as_view(), name='like_story'),
path('story/unlike/<int:pk>', UnlikeStory.as_view(), name='unlike_story'),
path('chapter/like/<int:pk>', LikeChapter.as_view(), name='like_chapter'),
path('chapter/unlike/<int:pk>', UnlikeChapter.as_view(), name='unlike_chapter'),
path('continuations/<int:pk>', StoryContinuations.as_view(), name='conts_story'),
path('continuations-chapter/<int:pk>', ChapterContinuations.as_view(), name='conts_chap'),
#path('create-resource', CreateResource.as_view(), name='create_resource'),
#path('edit-resource/<int:pk>', EditResource.as_view(), name='edit_resource'),
#path('resource/', ListUserResources.as_view(), name='user_resources_own'),
#path('resource-content/<int:pk>', JSONContentResource.as_view(), name='res_content'),
#path('search-tag/<tag>', JSONContentResource.as_view(), name='res_content'),
]

