from django.db import models
from django.utils import timezone


class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	Published_date = models.DateTimeField(blank=True, null=True)

def pubish(self):
	self.Published_date = timezone.now()
	self.save()

def __str__(self):
	return self.title
