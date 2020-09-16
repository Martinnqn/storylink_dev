
# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import StoryChapterSerializer, StoryPublicationSerializer

from ..models import StoryChapter, StoryPublication


class StoryPublicationViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = StoryPublication.objects.all()

    # specify serializer to be used
    serializer_class = StoryPublicationSerializer

# create a viewset


class StoryChapterViewSet(viewsets.ModelViewSet):
    queryset = StoryChapter.objects.all()

    # specify serializer to be used
    serializer_class = StoryChapterSerializer
