from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):						# Defines a model named Post. models.Model means that Post is a DJ model, so DJ knows it should be saved in the db
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)	# title, text are properties. models.CharField is how you define text with a limited number of characters
	text = models.TextField()
	created_date = models.DateTimeField(
		default = timezone.now)
	published_date = models.DateTimeField(
		blank = True, null = True)

	def publish(self):							# defining our publish method (def means this is a function/method)
		self.published_date = timezone.now()
		self.save()

	def __str__(self):							# we call __str__() to get a string with a Post title
		return self.title
