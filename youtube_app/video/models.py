from django.db import models

class Video(models.Model):
    id = models.CharField(max_length=255, null=False, primary_key=True) 
    title = models.CharField(max_length=255, null=False) # youtube has 100 char limit
    description = models.TextField()
    publishing_datetime = models.DateTimeField()
    thumbnails = models.JSONField()