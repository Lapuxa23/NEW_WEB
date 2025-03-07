from django.urls import path
from . import views

urlpatterns = [
    path('directors/', views.DirectorList.as_view(), name='director-list'),
    path('directors/<int:pk>/', views.DirectorDetail.as_view(), name='director-detail'),
    path('movies/', views.MovieList.as_view(), name='movie-list'),
    path('movies/<int:pk>/', views.MovieDetail.as_view(), name='movie-detail'),
    path('reviews/', views.ReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
]