from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

from .models import Movie

def index(request):
    """View function for home page of site."""

    # Generate counts of the movies
    num_movies = Movie.objects.all().count()
    context = {
        'num_movies': num_movies,
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class MovieListView(generic.ListView):
    model = Movie
    paginate_by = 5

class MovieDetailView(generic.DetailView):
    model = Movie

class MovieCreate(LoginRequiredMixin, CreateView):
    model = Movie
    fields = '__all__'

class MovieUpdate(LoginRequiredMixin, UpdateView):
    model = Movie
    fields = ['director', 'year', 'summary', 'genre']

class MovieDelete(LoginRequiredMixin, DeleteView):
    model = Movie
    success_url = reverse_lazy('movies')