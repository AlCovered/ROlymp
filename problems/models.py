from django.db import models


class Condition(models.Model):
    title = models.CharField(max_length=70)
    condition_itself = models.TextField()
    examples = models.TextField()
    explanation = models.TextField(blank=True)
    answer = models.TextField(default='Some')
    memory_limit = models.IntegerField()
    time_limit = models.FloatField()

    def __str__(self):
        return f'{self.title}'


class Code(models.Model):
    languages = (
        ('24', 'Python'),
        ('1', 'C#'),
        ('19', 'Prolog')
    )
    code_language = models.CharField(max_length=20, choices=languages, default='Python')
    code_itself = models.TextField()

    def __str__(self):
        return f'{self.code_language}'
