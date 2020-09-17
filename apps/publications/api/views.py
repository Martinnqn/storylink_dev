
# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import StoryChapterSerializer, StoryPublicationSerializer

from ..models import StoryChapter, StoryPublication

from rest_framework.permissions import IsAuthenticated


class StoryPublicationViewSet(viewsets.ModelViewSet):
    queryset = StoryPublication.objects.all()
    serializer_class = StoryPublicationSerializer
    permission_classes = (IsAuthenticated,)


class StoryChapterViewSet(viewsets.ModelViewSet):
    queryset = StoryChapter.objects.all()
    serializer_class = StoryChapterSerializer
