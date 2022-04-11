from .models import CustomUser
from sympy import true
from .models import test, IndexPhotos, Publications, PublicationsYears, PublicationsMembers, IntroduceUs, AlumniPhD, AlumniMs, OurLabTopic
from rest_framework import serializers, generics


class TestListSerializer(serializers.ModelSerializer):

    class Meta:
        model = test
        fields = ('id', 'title', 'des')


class IndexPhotosListSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = IndexPhotos
        fields = ("id", "title", "image", "image_url")

    def get_image_url(self, obj):
        request = self.context.get('request')
        image_url = obj.image.url
        if request:

            return request.build_absolute_uri(image_url)
        return


class PublicationListSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Publications
        fields = "__all__"

    def get_image_url(self, obj):
        request = self.context.get('request')
        image_url = obj.image.url
        if request:

            return request.build_absolute_uri(image_url)
        return


class PublicationListSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    members = serializers.SerializerMethodField()

    class Meta:
        model = Publications
        fields = "__all__"

    def get_image_url(self, obj):
        request = self.context.get('request')
        image_url = obj.image.url
        if request:

            return request.build_absolute_uri(image_url)
        return

    def get_members(self, obj):
        members = obj.Members.all()
        return PublicationsMebmersListSerializer(instance=members, many=True).data


class PublicationsYearsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicationsYears
        fields = "__all__"


class PublicationsMebmersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicationsMembers
        fields = "__all__"


class IntroduceUsListSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = IntroduceUs
        fields = "__all__"

    def get_image_url(self, obj):
        request = self.context.get('request')
        image_url = obj.image.url
        if request:
            return request.build_absolute_uri(image_url)
        return


class AlumniMsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlumniMs
        fields = "__all__"


class AlumniPhDListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlumniPhD
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'last_login', 'date_joined', 'is_staff')


class OurLabTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurLabTopic
        fields = '__all__'
