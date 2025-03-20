from rest_framework import serializers
from .models import Movie, MovieReview
from rest_framework.exceptions import ValidationError


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id name description duration created updated'.split()


class MovieReviewSerializer(serializers.ModelSerializer):
    movie_name = serializers.CharField(source='movie.name', read_only=True)

    class Meta:
        model = MovieReview
        fields = 'id text movie movie_name'.split()


class MovieValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, min_length=3, max_length=255)
    description = serializers.CharField(required=True)
    duration = serializers.IntegerField(min_value=1)

    def validate_name(self, name):
        if Movie.objects.filter(name=name).exists():
            raise ValidationError('Movie with this name already exists!')
        return name
