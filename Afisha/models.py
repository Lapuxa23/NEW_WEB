from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()

    def __str__(self):
        return self.title


class MovieReview(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.text[:50]