from django.db import models

# Create your models here.

class Question(models.Model):
    index = models.IntegerField(null=False, unique=True)
    question = models.CharField(max_length=150, null=False, blank=False)
    subscale = models.IntegerField(null=False)

    def __str__(self) -> str:
        return f'{self.question}'

class Answer(models.Model):
    user = models.CharField(max_length=150, null=False, blank=False)
    question_index = models.IntegerField(null=False)
    answer = models.IntegerField(null=False)

    def __str__(self) -> str:
        return f'User {self.user} answer {self.answer} to question {self.question_index}'
