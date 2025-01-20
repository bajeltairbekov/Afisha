from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieDerectorSerializer
from rest_framework import status
from .models import Director, Movie, Review




@api_view(http_method_names=['GET'])
def director_view(request):

    directors = Director.objects.all()

    list_ = DirectorSerializer(instance=directors, many=True).data

    return Response(data=list_)


@api_view(['GET'])
def director_id_view(request, id):
    try:
        directors = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'director not found'})


    data = DirectorSerializer(instance=directors).data

    return Response(data=data)










@api_view(http_method_names=['GET'])
def movie_view(request):
    movies = Movie.objects.all()

    list = MovieSerializer(instance=movies, many=True).data


    return Response(data=list)



@api_view(['GET'])
def movie_id_view(request, id):
    try:
        movies = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'movie not found'})


    data = MovieSerializer(instance=movies).data

    return Response(data=data)



@api_view(['GET'])
def review_view(request):
    reviews = Review.objects.all()

    list = ReviewSerializer(instance=reviews, many=True).data


    return Response(data=list)



@api_view(['GET'])
def review_id_view(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'review not found'})


    data = ReviewSerializer(instance=reviews).data

    return Response(data=data)

@api_view(['GET'])
def movies_reviews(request):
    reviews = Review.objects.all()

    list = ReviewSerializer(instance=reviews, many=True).data

    return Response(data=list)

@api_view(['GET'])
def directors_movie(request):
    movies = Movie.objects.all()

    list_ = MovieDerectorSerializer(instance=movies, many=True).data

    return Response(data=list_)
