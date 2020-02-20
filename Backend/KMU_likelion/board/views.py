from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .filters import (NoticeBoardCommentFilter, NoticeFilter,
                      QnABoardCommentFilter, QnAFilter,
                      StudyBoardCommentFilter, StudyFilter)
from .models import (NoticeBoard, NoticeBoardComment, QnABoard,
                     QnABoardComment, StudyBoard, StudyBoardComment)
from .serializers import (NoticeBoardCommentSerializer, NoticeBoardSerializer,
                          QnABoardCommentSerializer, QnABoardSerializer,
                          StudyBoardCommentSerializer, StudyBoardSerializer)


# 스터디 게시판 viewset
def like_status(self, request, *args, **kwargs):
    board = self.get_object()
    status = None

    if request.method == 'POST':
        # print("fdff",request.body) #react에서 request 요청을 받을때

        if board.like.filter(username=self.request.user.username).exists():

            board.like.remove(self.request.user.id)
            print("user removed(false) : ", board.like.filter(username=self.request.user.username).exists())
            status = False
        else:
            board.like.add(self.request.user.id)
            print("user added(true) : ", board.like.filter(username=self.request.user.username).exists())
            status = True

        return Response({"state": status})
    else:

        if board.like.filter(username=self.request.user.username).exists():

            status = True
        else:
            status = False

        return Response({"state": status})


def like_content(self, request, cat, *args, **kwargs):
    board_list = None
    serializer = None
    if cat == "study":
        board_list = self.request.user.study_like.all()
        serializer = StudyBoardSerializer(board_list, many=True)
    elif cat == "notice":
        board_list = self.request.user.notice_like.all()
        serializer = NoticeBoardSerializer(board_list, many=True)
    elif cat == "qna":
        board_list = self.request.user.qna_like.all()
        serializer = QnABoardSerializer(board_list, many=True)

    return Response({"board_contents": serializer.data})


class StudyViewSet(viewsets.ModelViewSet):
    queryset = StudyBoard.objects.all().order_by('pub_date')
    serializer_class = StudyBoardSerializer
    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]
    filter_class = StudyFilter

    @action(detail=False, methods=['POST'])
    def user_like(self, request, *args, **kwargs):
        cat = "study"
        return like_content(self, request, cat, *args, **kwargs)

    @action(detail=True, methods=['GET', 'POST'])
    def like(self, request, *args, **kwargs):
        return like_status(self, request, *args, **kwargs)

# 공지 게시판 viewset


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = NoticeBoard.objects.all().order_by('pub_date')

    # permission_classes = [
    #     permissions.IsAuthenticatedOrReadOnly,
    # ]

    serializer_class = NoticeBoardSerializer
    filter_class = NoticeFilter
    @action(detail=False, methods=['POST'])
    def user_like(self, request, *args, **kwargs):
        cat = "notice"
        return like_content(self, request, cat, *args, **kwargs)

    @action(detail=True, methods=['GET', 'POST'])
    def like(self, request, *args, **kwargs):
        return like_status(self, request, *args, **kwargs)


# QnA 게시판 viewset
class QnAViewSet(viewsets.ModelViewSet):
    queryset = QnABoard.objects.all().order_by('pub_date')
    serializer_class = QnABoardSerializer
    filter_class = QnAFilter
    @action(detail=False, methods=['POST'])
    def user_like(self, request, *args, **kwargs):
        cat = "qna"
        return like_content(self, request, cat, *args, **kwargs)

    @action(detail=True, methods=['GET', 'POST'])
    def like(self, request, *args, **kwargs):
        return like_status(self, request, *args, **kwargs)


# 스터디 댓글 viewset
class StudyCommentViewSet(viewsets.ModelViewSet):
    queryset = StudyBoardComment.objects.all().order_by('pub_date')
    serializer_class = StudyBoardCommentSerializer
    filter_class = StudyBoardCommentFilter


# 공지 댓글 viewset
class NoticeCommentViewSet(viewsets.ModelViewSet):
    queryset = NoticeBoardComment.objects.all().order_by('pub_date')
    serializer_class = NoticeBoardCommentSerializer
    filter_class = NoticeBoardCommentFilter


# QnA 댓글 viewset
class QnACommentViewSet(viewsets.ModelViewSet):
    queryset = QnABoardComment.objects.all().order_by('pub_date')
    serializer_class = QnABoardCommentSerializer
    filter_class = QnABoardCommentFilter