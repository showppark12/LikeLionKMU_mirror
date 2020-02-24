from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .filters import (
    CareerBoardFilter, NoticeBoardCommentFilter, NoticeBoardFilter,
    QnABoardCommentFilter, QnABoardFilter, SessionFilter,
    StudyBoardCommentFilter, StudyBoardFilter, SubmissionFilter)
from .models import (CareerBoard, NoticeBoard, NoticeBoardComment, QnABoard,
                     QnABoardComment, Score, Session, StudyBoard,
                     StudyBoardComment, Submission, SubmissionComment, SessionComment)
from .serializers import (AssignmentSerializer, CareerBoardSerializer,
                          LectureSerializer, NoticeBoardCommentSerializer,
                          NoticeBoardSerializer, QnABoardCommentSerializer,
                          QnABoardSerializer, RecommentSerializer,
                          ScoreSerializer, StudyBoardCommentSerializer,
                          StudyBoardSerializer, SubmissionSerializer,
                          SessionCommentSerializer, SubmissionCommentSerializer)


# 스터디 게시판 viewset
def like_status(self, request, *args, **kwargs):
    board = self.get_object()
    status = None

    if request.method == 'POST':
        # print("fdff",request.body) #react에서 request 요청을 받을때

        if board.like.filter(username=self.request.user.username).exists():

            board.like.remove(self.request.user.id)
            print("user removed(false) : ", board.like.filter(
                username=self.request.user.username).exists())
            status = False
        else:
            board.like.add(self.request.user.id)
            print("user added(true) : ", board.like.filter(
                username=self.request.user.username).exists())
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


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all().order_by('pub_date')
    serializer_class = LectureSerializer
    action_serializer_classes = {
        "assignments": AssignmentSerializer, "add_assignment": AssignmentSerializer}
    filter_class = SessionFilter

    def get_serializer_class(self):
        return self.action_serializer_classes.get(self.action, self.serializer_class)

    @action(detail=False, methods=['POST'])
    def user_like(self, request, *args, **kwargs):
        cat = "session"
        return like_content(self, request, cat, *args, **kwargs)

    @action(detail=True, methods=['GET', 'POST'])
    def like(self, request, *args, **kwargs):
        return like_status(self, request, *args, **kwargs)

    @action(detail=True, methods=['GET'])
    def assignments(self, request, *args, **kwargs):
        session = self.get_object()
        queryset = session.assignments.all()
        serializer = self.get_serializer(data=queryset, many=True)
        serializer.is_valid()
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def add_assignment(self, request, *args, **kwargs):
        session = self.get_object()
        assignment = session.add_assignment(**request.data)

        serializer = self.get_serializer(data=assignment)
        if session.session_type == session.ASSIGNMENT:
            raise serializer.ValidationError(
                "ASSIGNMENT Type Session must not have assignment")
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all().order_by('pub_date')
    serializer_class = SubmissionSerializer
    action_serializer_classes = {"scores": ScoreSerializer}
    filter_class = SubmissionFilter

    def get_serializer_class(self):
        return self.action_serializer_classes.get(self.action, self.serializer_class)

    @action(detail=False, methods=['POST'])
    def user_like(self, request, *args, **kwargs):
        cat = "session"
        return like_content(self, request, cat, *args, **kwargs)

    @action(detail=True, methods=['GET', 'POST'])
    def like(self, request, *args, **kwargs):
        return like_status(self, request, *args, **kwargs)

    @action(detail=True, methods=['GET', 'POST', 'PUT'])
    def scores(self, request, *args, **kwargs):
        submission = self.get_object()
        if request.method == 'POST':
            """
            TODO
            점수를 dictionary로 받아서 넣어주는거
            """
            serializer = self.get_serializer(many=True)
            serializer.is_valid()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            serializer = self.get_serializer(
                data=submission.scores.all(), many=True)
            serializer.is_valid()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)


class StudyViewSet(viewsets.ModelViewSet):
    queryset = StudyBoard.objects.all().order_by('pub_date')
    serializer_class = StudyBoardSerializer
    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]
    filter_class = StudyBoardFilter

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
    filter_class = NoticeBoardFilter
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
    filter_class = QnABoardFilter
    @action(detail=False, methods=['POST'])
    def user_like(self, request, *args, **kwargs):
        cat = "qna"
        return like_content(self, request, cat, *args, **kwargs)

    @action(detail=True, methods=['GET', 'POST'])
    def like(self, request, *args, **kwargs):
        return like_status(self, request, *args, **kwargs)


class CareerViewSet(viewsets.ModelViewSet):
    queryset = CareerBoard.objects.all().order_by('pub_date')
    serializer_class = CareerBoardSerializer
    filter_class = CareerBoardFilter

    @action(detail=False, methods=['POST'])
    def user_like(self, request, *args, **kwargs):
        cat = "career"
        return like_content(self, request, cat, *args, **kwargs)

    @action(detail=True, methods=['GET', 'POST'])
    def like(self, request, *args, **kwargs):
        return like_status(self, request, *args, **kwargs)


class SessionCommentViewSet(viewsets.ModelViewSet):
    queryset = SessionComment.objects.all().order_by('pub_date')
    serializer_class = SessionCommentSerializer


class SubmissionCommentViewSet(viewsets.ModelViewSet):
    queryset = SubmissionComment.objects.all().order_by('pub_date')
    serializer_class = SubmissionCommentSerializer


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

    def get_queryset(self):
        query = super().get_queryset()
        qs = query.filter(is_child=False)
        return qs

    def get_object(self):
        queryset = QnABoardComment.objects.all().order_by('pub_date')
        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, obj)

        return obj

    @action(detail=True, methods=['POST'])
    def re_comment(self, request, *args, **kwargs):
        comment = self.get_object()
        new_comment_dict = comment.re_comment(**request.data)

        serializer = self.get_serializer(data=new_comment_dict)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
