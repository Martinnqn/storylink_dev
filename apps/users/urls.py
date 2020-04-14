from django.urls import path, include

from . import views
from apps.users.views import *

app_name='user'

urlpatterns = [
    path('', ListUserPerfil.as_view(), name='user_profile'),
    path('followers/', ListUserFollowers.as_view(), name='user_followers'),
    path('following/', ListUserFollowing.as_view(), name='user_following'),
    path('stories-subscription/', ListStoriesSubscription.as_view(), name='user_stories_subscription'),
    path('follow/', FollowUser.as_view(), name='user_follow'),
    path('unfollow/', UnfollowUser.as_view(), name='user_unfollow'),
    path('delete/<int:id>', DeleteUser.as_view(), name='user_delete'),
    path('publication/', include('apps.publications.urls')),
    path('search/<suser>', SearchUser.as_view(), name='user_search')

]

