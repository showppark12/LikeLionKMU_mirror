from django.db import models
from polymorphic.models import PolymorphicModel
from datetime import datetime
# Create your models here.

class Board(PolymorphicModel):
    title = models.CharField(max_length=100) 
    body =  models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

#임시로 만든 column 임 나중에 수정가능
class StudyBoard(Board):
    how_many_people = models.IntegerField() #몇 명이 참가 했는가

class NoticeBoard(Board):
    # run_date = models.DateTimeField() #해당날짜
    run_date = models.DateTimeField(default=datetime.now, blank=True)

class QnABoard(Board):
    subject = models.CharField(max_length =100) #과목

class RecuitBoard(Board):
    purpose = models.CharField(max_length = 200) # 무슨 목적의 팀원 모집인지