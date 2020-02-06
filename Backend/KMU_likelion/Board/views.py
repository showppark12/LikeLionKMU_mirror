from rest_framework import viewsets, permissions
from .models import *
from .serializer import *
from rest_framework.decorators import action
from .pagination import *
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
# Create your views here.

#스터디 게시판 viewset
class StudyViewSet(viewsets.ModelViewSet):
    queryset = StudyBoard.objects.all().order_by('pub_date')
    serializer_class = StudySerializer
    pagination_class = Studypagination
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    @action(detail=True)

    def scrap(self,request,*args,**kwargs):
        board=self.get_object()
        
        status=None
        if board.scrap.filter(username=self.request.user.username).exists():
            board.scrap.remove(self.request.user.id)
            status=False
        else:
            board.scrap.add(self.request.user.id)
            status=True
        print(status)
        return Response({'status': status})


#공지 게시판 viewset
class NoticeViewSet(viewsets.ModelViewSet):
    queryset = NoticeBoard.objects.all().order_by('pub_date')

    permission_classes = [
        permissions.IsAuthenticated,
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
    queryset = RecuitBoard.objects.all().order_by('pub_date')
    serializer_class = RecuitSerializer 
    pagination_class = Recuitpagination



#스터디 댓글 viewset
class StudyCommentViewSet(viewsets.ModelViewSet):
    queryset = StudyComments.objects.all().order_by('pub_date')
    serializer_class = StudyCommentSerializer
    pagination_class = StudyCommentpagination
    def get_queryset(self):
        qs=super().get_queryset()
        search=self.request.query_params.get('search','')
        if search:
            qs=qs.filter(board=search)
        return qs

#공지 댓글 viewset
class NoticeCommentViewSet(viewsets.ModelViewSet):
    queryset = NoticeComments.objects.all().order_by('pub_date')
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    serializer_class = NoticeCommentSerializer
    pagination_class = NoticeCommentpagination
    
    def get_queryset(self):
        qs=super().get_queryset()
        search=self.request.query_params.get('search','')
        if search:
            qs=qs.filter(board=search)
        print('user : ',self.request.user)
        return qs
# QnA 댓글 viewset
class QnACommentViewSet(viewsets.ModelViewSet):
    queryset = QnAComments.objects.all().order_by('pub_date')
    serializer_class = QnACommentSerializer
    pagination_class = QnACommentpagination
    def get_queryset(self):
        qs=super().get_queryset()
        search=self.request.query_params.get('search','')
        if search:
            qs=qs.filter(board=search)
        return qs

# 팀원모집 댓글 viewset
class RecuitCommentViewSet(viewsets.ModelViewSet):
    queryset = RecuitComments.objects.all().order_by('pub_date')
    serializer_class = RecuitCommentSerializer
    pagination_class = RecuitCommentpagination
    def get_queryset(self):
        qs=super().get_queryset()
        search=self.request.query_params.get('search','')




        if search:
            qs=qs.filter(board=search)
        return qs
