from django.db import models


class AbstractNameModel(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Movie(AbstractNameModel):
    description = models.TextField()
    duration = models.IntegerField()


class MovieReview(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.text[:50]
