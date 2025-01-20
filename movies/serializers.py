from rest_framework import serializers
from .models import Director, Movie, Review

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'title description director genre search_word_list'.split()
        depth = 1

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name'.split()
        depth = 1


    def get_movies(self, Movie):
        movies = Movie.title

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'movie', 'text',  'stars']
        depth = 1


class MovieReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'movie, text, stars'.split()


class MovieDerectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'director title'.split()
        depth = 1










