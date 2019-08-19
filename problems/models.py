from django.db import models


class Condition(models.Model):
    title = models.CharField(max_length=70)
    condition_itself = models.TextField()
    examples = models.TextField()
    explanation = models.TextField(blank=True)
    memory_limit = models.IntegerField()
    time_limit = models.FloatField()

    def __str__(self):
        return f'{self.title}'
