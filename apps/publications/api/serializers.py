from ..models import StoryPublication, StoryChapter, Tag, StoryLike, \
    StoryChapter

from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag', ]


class StoryPublicationSerializer(serializers.HyperlinkedModelSerializer):
    tag = TagSerializer(many=True)
    cant_likes = serializers.CharField(source='get_cant_likes')

    class Meta:
        model = StoryPublication
        fields = ['url', 'title', 'text_content', 'img_content_link',
                  'date_time', 'status', 'cant_likes', 'color', 'tag']


class StoryChapterSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.CharField(source='quest_answ')
    tag = TagSerializer(many=True)
    cant_likes = serializers.CharField(source='get_cant_likes')

    class Meta:
        model = StoryChapter
        fields = ['url', 'title', 'text_content', 'date_time',
                  'cant_likes', 'color', 'tag']
