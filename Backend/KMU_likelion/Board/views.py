from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from rest_framework.decorators import action,api_view
from .pagination import *
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
import json
from .filterings import *



#스터디 게시판 viewset
def like_status(self,request,*args,**kwargs):
    board=self.get_object()
    status = None

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

            return Response({"state":status})
    else:
            
            if board.like.filter(username=self.request.user.username).exists():

                    status=True
            else:
                    status=False
          
            return Response({"state":status})

def like_content(self,request,cat,*args,**kwargs):
    board_list=None
    serializer=None
    if cat == "study":
        board_list=self.request.user.study_like.all()
        serializer=StudySerializer(board_list,many=True)
    elif cat == "notice":
         board_list=self.request.user.notice_like.all()
         serializer=NoticeSerializer(board_list,many=True)
    elif cat == "recruit":
        board_list=self.request.user.recruit_like.all()
        serializer=RecruitSerializer(board_list,many=True)
    elif cat == "qna":
        board_list=self.request.user.qna_like.all()
        serializer=QnASerializer(board_list,many=True)
    
    return Response({"board_contents":serializer.data})


class StudyViewSet(viewsets.ModelViewSet):
    queryset = StudyBoard.objects.all().order_by('pub_date')
    serializer_class = StudySerializer
    pagination_class = Studypagination
    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]     
    filter_class=StudyFilter

    @action(detail=False, methods = ['POST'])
    def user_like(self,request,*args,**kwargs):
        cat="study"
        return like_content(self,request,cat,*args,**kwargs)
    @action(detail=True, methods = ['GET','POST'])
    def like(self,request,*args,**kwargs):
        return like_status(self,request,*args,**kwargs)

#공지 게시판 viewset
class NoticeViewSet(viewsets.ModelViewSet): 
    queryset = NoticeBoard.objects.all().order_by('pub_date')

    # permission_classes = [
    #     permissions.IsAuthenticatedOrReadOnly,
    # ]

    serializer_class = NoticeSerializer
    pagination_class = Noticepagination
    filter_class=NoticeFilter
    @action(detail=False, methods = ['POST'])
    def user_like(self,request,*args,**kwargs):
        cat="notice"
        return like_content(self,request,cat,*args,**kwargs)
    
    @action(detail=True, methods = ['GET','POST'])
    def like(self,request,*args,**kwargs):
        return like_status(self,request,*args,**kwargs)


# QnA 게시판 viewset
class QnAViewSet(viewsets.ModelViewSet):
    queryset = QnABoard.objects.all().order_by('pub_date')
    serializer_class = QnASerializer
    pagination_class = QnApagination
    filter_class=QnAFilter
    @action(detail=False, methods = ['POST'])
    def user_like(self,request,*args,**kwargs):
        cat="qna"
        return like_content(self,request,cat,*args,**kwargs)

    @action(detail=True, methods = ['GET','POST'])
    def like(self,request,*args,**kwargs):
        return like_status(self,request,*args,**kwargs)


# 팀원모집 게시판 viewset
class RecruitViewSet(viewsets.ModelViewSet):
    queryset = RecruitBoard.objects.all().order_by('pub_date')
    serializer_class = RecruitSerializer 
    pagination_class = Recruitpagination
    filter_class=RecruitFilter
    @action(detail=False, methods = ['POST'])
    def user_like(self,request,*args,**kwargs):
        cat="recruit"
        return like_content(self,request,cat,*args,**kwargs)

    @action(detail=True, methods = ['GET','POST'])
    def like(self,request,*args,**kwargs):
        return like_status(self,request,*args,**kwargs)




#스터디 댓글 viewset
class StudyCommentViewSet(viewsets.ModelViewSet):
    queryset = StudyComments.objects.all().order_by('pub_date')
    serializer_class = StudyCommentSerializer
    pagination_class = StudyCommentpagination
    filter_class=StudyCommentFilter
 
 

#공지 댓글 viewset
class NoticeCommentViewSet(viewsets.ModelViewSet):
    queryset = NoticeComments.objects.all().order_by('pub_date')
    # permission_classes = [
    #     permissions.IsAuthenticatedOrReadOnly,
    # ]

    serializer_class = NoticeCommentSerializer
    pagination_class = NoticeCommentpagination
    filter_class=NoticeCommentFilter
   
    
  
# QnA 댓글 viewset
class QnACommentViewSet(viewsets.ModelViewSet):
    queryset = QnAComments.objects.all().order_by('pub_date')
    serializer_class = QnACommentSerializer
    pagination_class = QnACommentpagination
    filter_class=QnACommentFilter
  
   

# 팀원모집 댓글 viewset
class RecruitCommentViewSet(viewsets.ModelViewSet):
    queryset = RecruitComments.objects.all().order_by('pub_date')
    serializer_class = RecruitCommentSerializer
    pagination_class = RecruitCommentpagination
    filter_class=RecruitCommentFilter

