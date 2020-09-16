
# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import UserSerializer, UserProfileSerializer, \
    FullUserDataSerializer
from ..models import CustomUser, UserProfile


class UserViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = CustomUser.objects.all()

    # specify serializer to be used
    serializer_class = UserSerializer

# create a viewset


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()

    # specify serializer to be used
    serializer_class = UserProfileSerializer


class FullUserDataViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()

    # specify serializer to be used
    serializer_class = FullUserDataSerializer
