from django.db import models
from django.contrib.auth.models import AbstractUser


class StudyGroup(models.Model):
    title = models.CharField(max_length=300)
    pub_date = models.DateField()
    introduction = models.TextField()
    



class Profile(AbstractUser):
    major = models.CharField(max_length = 200, null=True)
    student_id = models.CharField(max_length = 200, null=True)
    is_manager=models.CharField(max_length = 200, null=True)
    start_number=models.CharField(max_length = 200, null=True)
    sns_id=models.CharField(max_length = 200, null=True)
    study = models.ForeignKey(StudyGroup, on_delete = models.CASCADE , related_name= "study_group", default = None)



class Record(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField()
    link = models.TextField()
    belong_to_user = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name="profile_record",default = None)

class Mentoring(models.Model):
    pub_date = models.DateField()
    mentor = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name="mentor",default = None)
    mentee = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name="mentee",default = None)

