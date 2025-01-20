
from django.contrib import admin
from django.urls import path
from movies import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.director_view),
    path('api/v1/directors/<int:id>/', views.director_id_view),
    path('api/v1/movies/', views.movie_view),
    path('api/v1/movies/<int:id>/', views.movie_id_view),
    path('api/v1/reviews/',views.review_view),
    path('api/v1/reviews/<int:id>/', views.review_id_view),
    path('api/v1/movies/reviews/', views.movies_reviews),
    path('api/v1/directorss/', views.directors_movie)
]
