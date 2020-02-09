from django.db import models
from accounts.models import User
# Create your models here.

class JoinForm(models.Model):
    name = models.CharField(max_length=200, null =True)
    phone_number = models.CharField(max_length=300, null =True)
    major = models.CharField(max_length=300, null =True)
    birth = models.DateField()
    sex = models.CharField(max_length=50, null =True)
    start_number = models.CharField(max_length=100, null =True)
    e_mail = models.CharField(max_length = 300, null =True)
    password = models.CharField(max_length=100, null =True)
    status = models.IntegerField( default = 0 ) # 0 심사중, 1 합격 2 나가리 

class Question(models.Model):
    body = models.TextField()

class Answer(models.Model):
    body  = models.TextField()
    joinform_id = models.ForeignKey(JoinForm, on_delete = models.CASCADE, related_name= "join_answer",default = None)
    question_id = models.ForeignKey(Question, on_delete = models.CASCADE, related_name= "question_answer",default = None)

class Evaluation(models.Model):
    joinform_id = models.ForeignKey(JoinForm, on_delete = models.CASCADE, related_name = "join_evaluation",default = None)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "user_evaluation",default = None)
    body = models.TextField()
    score= models.FloatField(default= 0.0)
    pub_date = models.DateTimeField(auto_now_add=True)
    


