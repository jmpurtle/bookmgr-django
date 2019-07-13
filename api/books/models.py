from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class Book(models.Model):
	title = models.CharField(max_length=512)
	subtitle = models.CharField(max_length=512)
	author = models.CharField(max_length=100)
	isbn = models.CharField(max_length=50)
	summary = models.TextField()
	description = models.TextField()
	publish_date = models.DateField()
	publisher = models.CharField(max_length=100)
	book_format = models.CharField(max_length=100)
	pages = models.IntegerField()
	loc_class = models.CharField(max_length=100)
	loc_ctrl = models.CharField(max_length=100)
	dewey = models.CharField(max_length=100)
	country = models.CharField(max_length=150)
	lang = models.CharField(max_length=30)
	book_status = models.CharField(max_length=50)
	cover = models.FileField()
	created = models.DateTimeField(default=timezone.now)
	updated = models.DateTimeField(auto_now=True)

class Genre(models.Model):
	name = models.CharField(max_length=100)
	books = models.ManyToManyField(Book, related_name="genres")

class Subject(models.Model):
	name = models.CharField(max_length=100)
	books = models.ManyToManyField(Book, related_name="subjects")