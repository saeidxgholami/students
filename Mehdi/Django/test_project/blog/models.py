from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=250)
	date_created =  models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now = True)
	content = models.TextField()

	def __str__(self):
		return self.title


class Person(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField(default=1)

	def __str__(self):
		return self.name