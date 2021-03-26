from django.urls import path

from .views import UserMigration

urlpatterns = [
  # /
  path('<suser>', UserMigration.as_view(), name='newevent'),
]
