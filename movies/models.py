from django.db import models



class Genre(models.Model):
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SearchWord(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    director = models.ForeignKey('Director', on_delete=models.PROTECT)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, null=True, blank=True)
    searchWord = models.ManyToManyField(SearchWord, blank=True)
    def __str__(self):
        return self.title

    def search_word_list(self):
        return [i.name for i in self.searchWord.all()]



GRADES = (
    (1, '*'),
    (2, '* *'),
    (3, '* * *'),
    (4, '* * * *'),
    (5, '* * * * *'),
)
class Review(models.Model):
    stars = models.IntegerField(choices=GRADES, default=1)
    text = models.TextField(null=True, blank=True)
    movie = models.ForeignKey('Movie', on_delete=models.PROTECT, related_name='reviews')

    def __str__(self):
        return self.text


