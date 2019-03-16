from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.MovieListView.as_view(), name='movies'),
    path('movie/<int:pk>', views.MovieDetailView.as_view(), name='movie-detail'),
    path('movie/create/', views.MovieCreate.as_view(), name='movie_create'),
    path('movie/<int:pk>/update/', views.MovieUpdate.as_view(), name='movie_update'),
    path('movie/<int:pk>/delete/', views.MovieDelete.as_view(), name='movie_delete'),
]

