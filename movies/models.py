from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    director = models.ForeignKey('Director', on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    movie = models.ForeignKey('Movie', on_delete=models.PROTECT)

    def __str__(self):
        return self.text
