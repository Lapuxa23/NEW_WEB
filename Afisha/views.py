from rest_framework import generics
from .models import Movie, MovieReview
from .serializers import MovieSerializer, MovieReviewSerializer


class MovieList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetail(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieReviewList(generics.ListAPIView):
    queryset = MovieReview.objects.all()
    serializer_class = MovieReviewSerializer


class MovieReviewDetail(generics.RetrieveAPIView):
    queryset = MovieReview.objects.all()
    serializer_class = MovieReviewSerializer
