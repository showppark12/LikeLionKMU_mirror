from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    major = models.CharField(max_length = 200, null=True)
    student_id = models.CharField(max_length = 200, null=True)
    is_manager=models.CharField(max_length = 200, null=True)
    start_number=models.CharField(max_length = 200, null=True)
    sns_id=models.CharField(max_length = 200, null=True)
   

class Record(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField()
    link = models.TextField()
    belong_to_user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="user_record",default = None)

class Mentoring(models.Model):
    pub_date = models.DateField()
    mentor = models.ForeignKey(User, on_delete = models.CASCADE, related_name="mentor",default = None)
    mentee = models.ForeignKey(User, on_delete = models.CASCADE, related_name="mentee",default = None)

class StudyGroup(models.Model):
    title = models.CharField(max_length=100) 
    pub_date = models.DateField(auto_now_add=True)
    introduction = models.TextField()

class StudyGroup_User(models.Model):
    participant = models.ForeignKey( User, on_delete= models.CASCADE,null=True)
    group = models.ForeignKey( StudyGroup, on_delete= models.CASCADE,null=True)
    