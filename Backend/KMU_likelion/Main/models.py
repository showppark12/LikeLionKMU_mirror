from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField 

from accounts.models import User
from Board.models import NoticeBoard

# Create your models here.

class Career(models.Model):
    title = models.CharField(max_length= 100)
    pub_date = models.DateTimeField(auto_now=True)
    link = models.URLField()
    participants = models.ManyToManyField(User,blank=True,related_name="career_user")
    body = RichTextUploadingField()

    def __str__(self):
        return self.title        

class Calender(models.Model):
    title = models.CharField(max_length= 100, null= True)
    start_date = models.DateField()
    end_date = models.DateField()
    contents = models.TextField()
    plan_type = models.IntegerField(default = 0) # 0이면 notice 1이면 normal
    notice_id = models.ForeignKey(NoticeBoard, on_delete = models.CASCADE , related_name= "calender", default = None, null = True)
    



