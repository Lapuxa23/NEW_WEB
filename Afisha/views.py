from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from .models import Movie, MovieReview
from .serializers import MovieSerializer, MovieReviewSerializer, MovieValidateSerializer


@api_view(http_method_names=['GET', 'POST'])
def movie_list_create_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(instance=movies, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)

        with transaction.atomic():
            movie = Movie.objects.create(
                name=serializer.validated_data.get('name'),
                description=serializer.validated_data.get('description'),
                duration=serializer.validated_data.get('duration')
            )

        return Response(data=MovieSerializer(movie).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = MovieSerializer(movie).data
        return Response(data=data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        movie.name = serializer.validated_data.get('name')
        movie.description = serializer.validated_data.get('description')
        movie.duration = serializer.validated_data.get('duration')
        movie.save()
        return Response(data=MovieSerializer(movie).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def movie_review_list_create_api_view(request):
    if request.method == 'GET':
        reviews = MovieReview.objects.select_related('movie').all()
        serializer = MovieReviewSerializer(instance=reviews, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = MovieReviewSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)

        review = MovieReview.objects.create(
            text=serializer.validated_data.get('text'),
            movie_id=serializer.validated_data.get('movie').id
        )
        return Response(data=MovieReviewSerializer(review).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE'])
def movie_review_detail_api_view(request, id):
    try:
        review = MovieReview.objects.get(id=id)
    except MovieReview.DoesNotExist:
        return Response(data={'error': 'Review not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        return Response(data=MovieReviewSerializer(review).data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
