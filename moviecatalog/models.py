from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Genre(models.Model):
    """Model representing a movie genre."""
    name = models.CharField(max_length=200, help_text='Enter a movie genre')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Movie(models.Model):
    """Model representing a movie."""
    
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    year = models.IntegerField()
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the movie')
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this movie')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this movie."""
        return reverse('movie-detail', args=[str(self.id)])

    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    
    display_genre.short_description = 'Genre'



