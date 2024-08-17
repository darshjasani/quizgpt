# quiz/models.py

from django.db import models

class PDF(models.Model):
    file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class QuizSettings(models.Model):
    pdf = models.OneToOneField(PDF, on_delete=models.CASCADE)
    easy_questions = models.IntegerField(default=0)
    medium_questions = models.IntegerField(default=0)
    hard_questions = models.IntegerField(default=0)