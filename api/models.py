from tastypie.resources import ModelResource

from django.db import models
from movies.models import Movie

# Create your models here.
class MovieResource(ModelResource):
  class Meta:
    queryset = Movie.objects.all()
    resource_name = 'movies' 

