from django.db import models

# Create your models here.
class MediaSect(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    text = models.TextField(blank=True)
    video = models.URLField(blank=True)
    file = models.FileField(upload_to='static/files', blank=True, null=True)
    image = models.ImageField(upload_to='static/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)