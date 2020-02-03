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



#스터디 댓글 viewset
class StudyCommentViewSet(viewsets.ModelViewSet):
    queryset = StudyComments.objects.all()
    serializer_class = StudyCommentSerializer

#공지 댓글 viewset
class NoticeCommentViewSet(viewsets.ModelViewSet):
    queryset = NoticeComments.objects.all()
    serializer_class = NoticeCommentSerializer

# QnA 댓글 viewset
class QnACommentViewSet(viewsets.ModelViewSet):
    queryset = QnAComments.objects.all()
    serializer_class = QnACommentSerializer

# 팀원모집 댓글 viewset
class RecuitCommentViewSet(viewsets.ModelViewSet):
    queryset = RecuitComments.objects.all()
    serializer_class = RecuitCommentSerializer 
