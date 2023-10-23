from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Tag, Video, Ratings, Dashboard

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "last_login",
            "is_superuser",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_active",
        ]
        read_only_fields = ['username']


class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ('id', 'rating',)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name',)


class VideoSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    ratings = RatingsSerializer(many=True)

    class Meta:
        model = Video
        fields = ('id', 'url', 'title', 'description', 'ratings', 'tags', 'created_at', 'updated_at')


class DashboardSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    videos = VideoSerializer(many=True)

    class Meta:
        model = Dashboard
        fields = '__all__'


class RatingUpdateSerializer(serializers.Serializer):
    rating = serializers.IntegerField()
