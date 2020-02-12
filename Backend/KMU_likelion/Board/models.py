from django.db import models
from accounts.models import *
# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=200) 
    body =  models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True) #게시물 등록 시간 생성 
    update_date = models.DateTimeField(auto_now=True) # 업데이트 될 때만 정보 바뀔때 마다
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, default = None)
    class Meta:
        abstract = True

class StudyBoard(Board):
    study_type = models.IntegerField( default = 0) # 0: 공식모임, 1: 정보공유 2: etc
    personnel = models.IntegerField(default = 0)
    group_id = models.ForeignKey(StudyGroup, on_delete =models.CASCADE, related_name= "group_board", default = None)
    like = models.ManyToManyField(User, blank=True,related_name="study_like")
    def total_likes(self):
        return self.like.count()

class NoticeBoard(Board):
    notice_date = models.DateField(null = True)
    like = models.ManyToManyField(User, blank=True,related_name="notice_like")
    def total_likes(self):
        return self.like.count()

class RecruitBoard(Board):
    purpose = models.CharField(max_length= 100)
    like = models.ManyToManyField(User, blank=True,related_name="recruit_like")
    def total_likes(self):
        return self.like.count()

class QnABoard(Board):
    subject = models.CharField(max_length= 200)
    like = models.ManyToManyField(User, blank=True,related_name="qna_like")
    def total_likes(self):
        return self.like.count() 

class Comments(models.Model):
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)  
    update_date = models.DateTimeField(auto_now=True) 
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, default = None)
    class Meta:
        abstract = True

class StudyComments(Comments):
    board = models.ForeignKey( StudyBoard, on_delete= models.CASCADE, related_name= "study_comments")

class NoticeComments(Comments):
    board = models.ForeignKey( NoticeBoard, on_delete= models.CASCADE, related_name= "notice_comments")

class QnAComments(Comments):
    board = models.ForeignKey( QnABoard, on_delete= models.CASCADE, related_name= "QnA_comments")

class RecruitComments(Comments):
    board = models.ForeignKey( RecruitBoard, on_delete= models.CASCADE, related_name= "recruit_comments")