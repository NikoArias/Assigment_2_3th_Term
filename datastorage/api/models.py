from django.db import models



class Counter(models.Model): # This is called a "table" in a database. In django it's called a "model".
    value = models.IntegerField()  # This is called the "column" in a database. In django it's called a "field".



class Comment(models.Model):
    text = models.TextField()



class Product(models.Model):
    price = models.FloatField()
    name = models.TextField()
    currency = models.TextField()

class FavMusic(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

class Song(models.Model):
    title = models.TextField()
    artist = models.TextField()
    year = models.IntegerField()

class Movie(models.Model):
    name = models.TextField()
    studio = models.TextField()
    release = models.IntegerField()
