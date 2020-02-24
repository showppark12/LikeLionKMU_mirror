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


class BaseBoardViewSet(viewsets.ModelViewSet):
    action_serializer_classes = {}
    
    def get_serializer_class(self):
        return self.action_serializer_classes.get(self.action, self.serializer_class)

    @action(detail=False, methods=['POST'])
    def user_like(self, request, *args, **kwargs):
        board_list = None
        if self.category == "study":
            board_list = request.user.study_like.all()
        elif self.category == "notice":
            board_list = request.user.notice_like.all()
        elif self.category == "qna":
            board_list = request.user.qna_like.all()
        elif self.category == "career":
            board_list = request.user.career_like.all()
        elif self.category == "session":
            board_list = request.user.session_like.all()
        elif self.category == "submission":
            board_list = request.user.submission_like.all()

        serializer = self.get_serializer(board_list, many=True)
        return Response({"board_contents": serializer.data})

    @action(detail=True, methods=['GET', 'POST'])
    def like(self, request, *args, **kwargs):
        board = self.get_object()
        status = None
        alread_liked = board.like.filter(username=request.user.username).exists()

        if request.method == 'POST':
            status = not alread_liked
            if alread_liked:
                board.like.remove(request.user.id)
                print("user removed(false) : ", alread_liked)
            else:
                board.like.add(request.user.id)
                print("user added(true) : ", alread_liked)
        else:
            status = alread_liked
        return Response({"state": status})


class SessionViewSet(BaseBoardViewSet):
    queryset = Session.objects.all()
    serializer_class = LectureSerializer
    action_serializer_classes = {
        "assignments": AssignmentSerializer, "add_assignment": AssignmentSerializer}
    filter_class = SessionFilter
    category = "session"

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
        print(request.data)

        serializer = self.get_serializer(data=assignment)
        if session.session_type == session.ASSIGNMENT:
            raise serializer.ValidationError(
                "ASSIGNMENT Type Session must not have assignment")
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class SubmissionViewSet(BaseBoardViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    action_serializer_classes = {"scores": ScoreSerializer}
    filter_class = SubmissionFilter
    category = "submission"
    
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


class StudyViewSet(BaseBoardViewSet):
    queryset = StudyBoard.objects.all()
    serializer_class = StudyBoardSerializer
    filter_class = StudyBoardFilter
    category = "study"


# 공지 게시판 viewset
class NoticeViewSet(BaseBoardViewSet):
    queryset = NoticeBoard.objects.all()
    serializer_class = NoticeBoardSerializer
    filter_class = NoticeBoardFilter
    category = "notice"


# QnA 게시판 viewset
class QnAViewSet(BaseBoardViewSet):
    queryset = QnABoard.objects.all()
    serializer_class = QnABoardSerializer
    filter_class = QnABoardFilter
    category = "qna"


class CareerViewSet(BaseBoardViewSet):
    queryset = CareerBoard.objects.all()
    serializer_class = CareerBoardSerializer
    filter_class = CareerBoardFilter
    category = "career"


class SessionCommentViewSet(viewsets.ModelViewSet):
    queryset = SessionComment.objects.all()
    serializer_class = SessionCommentSerializer


class SubmissionCommentViewSet(viewsets.ModelViewSet):
    queryset = SubmissionComment.objects.all()
    serializer_class = SubmissionCommentSerializer


# 스터디 댓글 viewset
class StudyCommentViewSet(viewsets.ModelViewSet):
    queryset = StudyBoardComment.objects.all()
    serializer_class = StudyBoardCommentSerializer
    filter_class = StudyBoardCommentFilter


# 공지 댓글 viewset
class NoticeCommentViewSet(viewsets.ModelViewSet):
    queryset = NoticeBoardComment.objects.all()
    serializer_class = NoticeBoardCommentSerializer
    filter_class = NoticeBoardCommentFilter


# QnA 댓글 viewset
class QnACommentViewSet(viewsets.ModelViewSet):
    queryset = QnABoardComment.objects.all()
    serializer_class = QnABoardCommentSerializer
    filter_class = QnABoardCommentFilter

    def get_queryset(self):
        query = super().get_queryset()
        qs = query.filter(is_child=False)
        return qs

    def get_object(self):
        queryset = QnABoardComment.objects.all()
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
