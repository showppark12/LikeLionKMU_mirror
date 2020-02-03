from django.db import models

# Create your models here.

class JoinForm(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=300)
    major = models.CharField(max_length=300)
    e_mail = models.CharField(max_length = 300)

class Question(models.Model):
    question_id = models.IntegerField()
    question = models.TextField()

class Answer(models.Model):
    answer  = models.TextField()
    belong_to_join = models.ForeignKey(JoinForm, on_delete = models.CASCADE, related_name= "join_answer")
    belong_to_question = models.ForeignKey(Question, on_delete = models.CASCADE, related_name= "question_answer")
