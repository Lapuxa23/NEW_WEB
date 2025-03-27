from rest_framework import generics, status
from rest_framework.response import Response
from django.db import transaction
from .models import Movie, MovieReview
from .serializers import MovieSerializer, MovieReviewSerializer, MovieValidateSerializer


class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def create(self, request, *args, **kwargs):
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            movie = Movie.objects.create(**serializer.validated_data)

        return Response(MovieSerializer(movie).data, status=status.HTTP_201_CREATED)


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        for attr, value in serializer.validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return Response(MovieSerializer(instance).data, status=status.HTTP_200_OK)


class MovieReviewListCreateView(generics.ListCreateAPIView):
    queryset = MovieReview.objects.select_related('movie').all()
    serializer_class = MovieReviewSerializer

    def create(self, request, *args, **kwargs):
        serializer = MovieReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        review = MovieReview.objects.create(
            text=serializer.validated_data.get('text'),
            movie=serializer.validated_data.get('movie')
        )

        return Response(MovieReviewSerializer(review).data, status=status.HTTP_201_CREATED)


class MovieReviewDetailView(generics.RetrieveDestroyAPIView):
    queryset = MovieReview.objects.all()
    serializer_class = MovieReviewSerializer
