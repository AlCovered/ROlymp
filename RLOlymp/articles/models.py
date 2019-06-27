from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150)
    short_description = models.TextField()

    def __str__(self):
        return f'{self.title}'
