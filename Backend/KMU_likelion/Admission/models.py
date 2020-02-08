from django.db import models
from accounts.models import User
# Create your models here.

class JoinForm(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=300)
    major = models.CharField(max_length=300)
    birth = models.DateField()
    sex = models.CharField(max_length=50)
    major = models.CharField(max_length=100)
    e_mail = models.CharField(max_length = 300)

class Question(models.Model):
    body = models.TextField()

class Answer(models.Model):
    body  = models.TextField()
    joinform_id = models.ForeignKey(JoinForm, on_delete = models.CASCADE, related_name= "join_answer")
    question_id = models.ForeignKey(Question, on_delete = models.CASCADE, related_name= "question_answer")

class Evaluation(models.Model):
    joinform_id = models.ForeignKey(JoinForm, on_delete = models.CASCADE, related_name = "join_evaluation",default = None)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "user_evaluation",default = None)
    body = models.TextField()
    score= models.FloatField(default= 0.0)
    pub_date = models.DateTimeField(auto_now_add=True)
    


