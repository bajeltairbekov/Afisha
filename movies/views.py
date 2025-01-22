from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieDerectorSerializer, \
    MovieItmeSerializer, ReviewItmeSerializer
from rest_framework import status
from .models import Director, Movie, Review


@api_view(http_method_names=['GET', 'POST'])
def director_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()

        list_ = DirectorSerializer(instance=directors, many=True).data

        return Response(data=list_)

    elif request.method == 'POST':
        name = request.data.get('name')

        director = Director.objects.create(
            name=name
        )
        return Response(status=status.HTTP_201_CREATED,
                        data=DirectorSerializer(director).data)



@api_view(['GET', 'PUT', 'DELETE'])
def director_id_view(request, id):
    try:
        directors = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'director not found'})
    if request.method == 'GET':
        data = DirectorSerializer(instance=directors).data

        return Response(data=data)
    elif request.method == 'PUT':
        directors.name = request.data.get('name')

        return Response(data=DirectorSerializer(directors).data,
                        status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        directors.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(http_method_names=['GET', 'POST'])
def movie_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()

        list = MovieSerializer(instance=movies, many=True).data

        return Response(data=list)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        director_id = request.data.get('director_id')
        searchWord = request.data.get('searchWord')
        genre_id = request.data.get('genre_id')

        movie = Movie.objects.create(
            title=title,
            description=description,
            director_id=director_id,
            genre_id=genre_id
        )
        movie.searchWord.set(searchWord)
        movie.save()

        return Response(status=status.HTTP_201_CREATED,
                        data=MovieItmeSerializer(movie).data)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_id_view(request, id):

    try:
        movies = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'movie not found'})
    if request.method == 'GET':
        data = MovieSerializer(instance=movies).data

        return Response(data=data)

    elif request.method == 'PUT':
        movies.title = request.data.get('title')
        movies.description = request.data.get('description')
        return Response(data=MovieItmeSerializer(movies).data,
                        status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def review_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()

        list = ReviewSerializer(instance=reviews, many=True).data

        return Response(data=list)
    elif request.method == 'POST':
        stars = request.data.get('stars')
        text = request.data.get('text')
        movie_id = request.data.get('movie_id')

        review = Review.objects.create(
            stars=stars,
            text=text,
            movie_id=movie_id
        )
        return Response(status=status.HTTP_201_CREATED,
                        data=ReviewItmeSerializer(review).data)



@api_view(['GET', 'PUT', 'DELETE'])
def review_id_view(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'review not found'})
    if request.method == 'GET':
        data = ReviewSerializer(instance=reviews).data

        return Response(data=data)
    elif request.method == 'PUT':
        reviews.text = request.data.get('text')
        reviews.stars = request.data.get('stars')
        return Response(data=ReviewSerializer(reviews).data,
                        status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        reviews.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
