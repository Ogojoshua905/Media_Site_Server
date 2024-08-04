from django.db import models
from django.utils import timezone  # Correct import

class MediaSect(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    text = models.TextField(blank=True)
    video = models.FileField(upload_to='medias/videos', blank=True)
    pdf = models.FileField(upload_to='static/files', blank=True, null=True)
    image = models.ImageField(upload_to='static/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title