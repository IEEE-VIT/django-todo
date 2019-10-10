from django.db import models


class Tasks(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	deadline = models.DateTimeField()
	done = models.BooleanField(default=False)