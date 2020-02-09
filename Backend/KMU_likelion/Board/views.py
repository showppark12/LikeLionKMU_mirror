from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from rest_framework.decorators import action
from .pagination import *
from rest_framework.filters import SearchFilter
from rest_framework.response import Response


#스터디 게시판 viewset


class StudyViewSet(viewsets.ModelViewSet):
    queryset = StudyBoard.objects.all().order_by('pub_date')
    serializer_class = StudySerializer
    pagination_class = Studypagination
    permission_classes = [
        permissions.IsAuthenticated,
    ]     

#공지 게시판 viewset
class NoticeViewSet(viewsets.ModelViewSet):
    queryset = NoticeBoard.objects.all().order_by('pub_date')

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]

    serializer_class = NoticeSerializer
    pagination_class = Noticepagination
    


# QnA 게시판 viewset
class QnAViewSet(viewsets.ModelViewSet):
    queryset = QnABoard.objects.all().order_by('pub_date')
    serializer_class = QnASerializer
    pagination_class = QnApagination

# 팀원모집 게시판 viewset
class RecuitViewSet(viewsets.ModelViewSet):
    queryset = RecruitBoard.objects.all().order_by('pub_date')
    serializer_class = RecruitSerializer 
    pagination_class = Recruitpagination



#스터디 댓글 viewset
class StudyCommentViewSet(viewsets.ModelViewSet):
    queryset = StudyComments.objects.all().order_by('pub_date')
    serializer_class = StudyCommentSerializer
    pagination_class = StudyCommentpagination
    def get_queryset(self):
        qs=super().get_queryset()
        board_id=self.request.query_params.get('id','')
        if board_id:
            qs=qs.filter(board=board_id)
        return qs
 

#공지 댓글 viewset
class NoticeCommentViewSet(viewsets.ModelViewSet):
    queryset = NoticeComments.objects.all().order_by('pub_date')
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]

    serializer_class = NoticeCommentSerializer
    pagination_class = NoticeCommentpagination

    def get_queryset(self):
        qs=super().get_queryset()
        board_id=self.request.query_params.get('id','')
        if board_id:
            qs=qs.filter(board=board_id)
        return qs
    
  
# QnA 댓글 viewset
class QnACommentViewSet(viewsets.ModelViewSet):
    queryset = QnAComments.objects.all().order_by('pub_date')
    serializer_class = QnACommentSerializer
    pagination_class = QnACommentpagination
  
    def get_queryset(self):
        qs=super().get_queryset()
        board_id=self.request.query_params.get('id','')
        if board_id:
            qs=qs.filter(board=board_id)
        return qs

# 팀원모집 댓글 viewset
class RecuitCommentViewSet(viewsets.ModelViewSet):
    queryset = RecruitComments.objects.all().order_by('pub_date')
    serializer_class = RecruitCommentSerializer
    pagination_class = RecruitCommentpagination
   

    def get_queryset(self):
        qs=super().get_queryset()
        board_id=self.request.query_params.get('id','')
        if board_id:
            qs=qs.filter(board=board_id)
        return qs