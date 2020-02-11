from django.db import models
from accounts.models import User
# Create your models here.

class JoinForm(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=50, unique= True)
    student_id = models.CharField(max_length=50, default=None)
    birth = models.DateField()
    sex = models.CharField(max_length=50, null =True)
    major = models.CharField(max_length=50, null =True)
    email = models.CharField(max_length = 50, null =True)
    pw = models.CharField(max_length=50, null =True)
    status = models.IntegerField( default = 0 ) # 0 심사중, 1 합격 2 나가리 
    pub_date = models.DateTimeField(auto_now_add=True) #게시물 등록 시간 생성 
    update_date = models.DateTimeField(auto_now=True) # 업데이트 될 때만 정보 바뀔때 마다

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
    


