from django.urls import path
from .views import (
    movie_list_create_api_view,
    movie_detail_api_view,
    movie_review_list_create_api_view,
    movie_review_detail_api_view,
)

urlpatterns = [
    path('movies/', movie_list_create_api_view, name='movie-list-create'),
    path('movies/<int:id>/', movie_detail_api_view, name='movie-detail'),
    path('reviews/', movie_review_list_create_api_view, name='movie-review-list-create'),
    path('reviews/<int:id>/', movie_review_detail_api_view, name='movie-review-detail'),
]
