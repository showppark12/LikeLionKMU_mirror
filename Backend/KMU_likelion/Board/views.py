from rest_framework import viewsets
from .models import *
from .serializer import *
from rest_framework.decorators import action

# Create your views here.

#스터디 게시판 viewset
class StudyViewSet(viewsets.ModelViewSet):
    queryset = StudyBoard.objects.all()
    serializer_class = StudySerializer

#공지 게시판 viewset
class NoticeViewSet(viewsets.ModelViewSet):
    queryset = NoticeBoard.objects.all()
    serializer_class = NoticeSerializer

# QnA 게시판 viewset
class QnAViewSet(viewsets.ModelViewSet):
    queryset = QnABoard.objects.all()
    serializer_class = QnASerializer

# 팀원모집 게시판 viewset
class RecuitViewSet(viewsets.ModelViewSet):
    queryset = RecuitBoard.objects.all()
    serializer_class = RecuitSerializer 