from django.db import models
from polymorphic.models import PolymorphicModel
from django.conf import settings
from datetime import datetime
from account.models import *
# Create your models here.

class Board(PolymorphicModel):
    title = models.CharField(max_length=100) 
    body =  models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True) #게시물 등록 시간 생성 
    update_date = models.DateTimeField(auto_now=True) # 업데이트 될 때만 정보 바뀔때 마다
    writer = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "writer", default = None)
    scrap=models.ManyToManyField(User, blank=True,related_name="board_scrap")


#임시로 만든 column 임 나중에 수정가능
class StudyBoard(Board):
    how_many_people = models.IntegerField() #몇 명이 참가 했는
    group = models.ForeignKey( StudyGroup, on_delete= models.CASCADE,null=True)
class NoticeBoard(Board):
    run_date = models.DateField( default = datetime.now , blank = True) # 해당날짜

class QnABoard(Board):
    subject = models.CharField(max_length =100) #과목

class RecuitBoard(Board):
    purpose = models.CharField(max_length = 200) # 무슨 목적의 팀원 모집인지



#댓글 모델
class Comments(PolymorphicModel):
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)  
    update_date = models.DateTimeField(auto_now=True) 
    writer = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "comment_writer", default = None)

class StudyComments(Comments):
    board = models.ForeignKey( StudyBoard, on_delete= models.CASCADE, related_name= "study_comments")

class NoticeComments(Comments):
    board = models.ForeignKey( NoticeBoard, on_delete= models.CASCADE, related_name= "notice_comments")

class QnAComments(Comments):
    board = models.ForeignKey( QnABoard, on_delete= models.CASCADE, related_name= "QnA_comments")

class RecuitComments(Comments):
    board = models.ForeignKey( RecuitBoard, on_delete= models.CASCADE, related_name= "recuit_comments")

