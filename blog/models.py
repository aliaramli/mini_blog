from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.

STATUS = (
        (0, "Draft"),
        (1, "Pending"),
        (2, "Publish")
        )

class Post(models.Model):
    # GOOGLE will cut off too long title length search result
    # Thus i set as 60 char.
    title = models.CharField(max_length=60, unique=True)
    # Shorter slug also easy to be processed by GOOGLE
    slug  = models.SlugField(max_length=60, unique=True)
    author = models.ForeignKey (User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    cover = models.ImageField(upload_to='images/', default='images/default.png')
    content = models.TextField( blank=True)
    created_on = models.DateTimeField(auto_now = True)
    status = models.IntegerField(choices=STATUS, default=0)
    tags = TaggableManager()
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

from time import sleep
import re
from datetime import datetime, timedelta
import requests

class Data():
    def __init__(self, data):
        self.confirmed = data[0]['confirmed']
        self.dead = data[0]['dead']
        self.recovered = data[0]['recovered']

class Coronavirus():
    def __init__(self): 
        pass

    def get_data(self):
        payload = {"country_code":"MY", "start_date": datetime.today().strftime('%Y-%m-%d'), "end_date": (datetime.today()+timedelta(days=1)).strftime('%Y-%m-%d')}
        response = requests.get("http://api.coronatracker.com/analytics/trend/country", params=payload)
        return Data(response.json())
