from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	datePosted = models.DateTimeField(default= timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	

	def __str__(self):
		return self.title

class Threads(models.Model):
	threadName = models.CharField(max_length=30)
	threadDescription = models.TextField()
	datePosted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.threadName

