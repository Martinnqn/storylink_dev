
# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import UserSerializer, UserProfileSerializer, \
    FullUserDataSerializer, WhoamiSerializer
from ..models import CustomUser, UserProfile

from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class WhoamiViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = WhoamiSerializer
    permission_classes = (IsAuthenticated,)
    basename = 'whoami'

    def get_queryset(self):
        return CustomUser.objects.filter(username=self.request.user.username)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class FullUserDataViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = FullUserDataSerializer
