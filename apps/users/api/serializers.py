from ..models import CustomUser, UserProfile, UserSubscriptionModelAux, \
    PubSubscriptionModelAux

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['url', 'username', 'email', ]


class UserSubscriptionModelAuxSerializer(serializers.Serializer):
    to_user = UserSerializer(source='to_user.user')

    class Meta:
        model = UserSubscriptionModelAux
        fields = ['to_user']


class PubSubscriptionModelAuxSerializer(serializers.Serializer):
    pub = serializers.CharField(source='pub.title')

    class Meta:
        model = PubSubscriptionModelAux
        fields = ['pub']


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    user_subscription = UserSubscriptionModelAuxSerializer(source='from2To',
                                                           read_only=True, many=True)
    pub_subscription = PubSubscriptionModelAuxSerializer(
        source='user2Pub', many=True)

    class Meta:
        model = UserProfile
        fields = ['url', 'id', 'link_img_perfil', 'description',
                  'pub_subscription', 'user_subscription']


class FullUserDataSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(source='profile.get', read_only=True)

    class Meta:
        model = CustomUser
        fields = ['url', 'username', 'email', 'profile']
