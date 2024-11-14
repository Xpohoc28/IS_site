from django.db import models


class News(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)

    def __str__(self):
        return self.title
# Create your models here.
