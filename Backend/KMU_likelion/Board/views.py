from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from rest_framework.decorators import action,api_view
from .pagination import *
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
import json


#스터디 게시판 viewset
def like_status(self,request,*args,**kwargs):
    board=self.get_object()
    status=None
    if request.method == 'POST':
        # print("fdff",request.body) #react에서 request 요청을 받을때
            if board.like.filter(username=self.request.user.username).exists():
                    board.like.remove(self.request.user.id)
                    print("user removed(false) : ",board.like.filter(username=self.request.user.username).exists())
                    status=False
            else:
                    board.like.add(self.request.user.id)
                    print("user added(true) : ",board.like.filter(username=self.request.user.username).exists())
                    status=True
            return Response({'status': status})
    else:
            if board.like.filter(username=self.request.user.username).exists():
                    status=True
            else:
                    status=False
        
            return Response({'status': status})
  



class StudyViewSet(viewsets.ModelViewSet):
    queryset = StudyBoard.objects.all().order_by('pub_date')
    serializer_class = StudySerializer
    pagination_class = Studypagination
    permission_classes = [
        permissions.IsAuthenticated,
    ]     


    @action(detail=True, methods = ['GET','POST'])
    def like(self,request,*args,**kwargs):
        return like_status(self,request,*args,**kwargs)

#공지 게시판 viewset
class NoticeViewSet(viewsets.ModelViewSet): 
    queryset = NoticeBoard.objects.all().order_by('pub_date')

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]

    serializer_class = NoticeSerializer
    pagination_class = Noticepagination

    @action(detail=True, methods = ['GET','POST'])
    def like(self,request,*args,**kwargs):
        return like_status(self,request,*args,**kwargs)


# QnA 게시판 viewset
class QnAViewSet(viewsets.ModelViewSet):
    queryset = QnABoard.objects.all().order_by('pub_date')
    serializer_class = QnASerializer
    pagination_class = QnApagination

    @action(detail=True, methods = ['GET','POST'])
    def like(self,request,*args,**kwargs):
        return like_status(self,request,*args,**kwargs)


# 팀원모집 게시판 viewset
class RecuitViewSet(viewsets.ModelViewSet):
    queryset = RecruitBoard.objects.all().order_by('pub_date')
    serializer_class = RecruitSerializer 
    pagination_class = Recruitpagination

    @action(detail=True, methods = ['GET','POST'])
    def like(self,request,*args,**kwargs):
        return like_status(self,request,*args,**kwargs)




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