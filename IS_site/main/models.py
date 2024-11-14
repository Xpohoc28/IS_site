from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    image_url = models.URLField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title