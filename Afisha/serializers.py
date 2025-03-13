from rest_framework import serializers
from .models import Movie, MovieReview


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration']


class MovieReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieReview
        fields = ['id', 'text', 'movie']