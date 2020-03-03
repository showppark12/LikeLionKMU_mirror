import rest_framework
from django.shortcuts import get_object_or_404
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .permission import IsAuthorOrReadonly, IsStudyMemberOrReadonly, IsStaffOrReadonly
from . import filters, models, serializers
from rest_framework.permissions import AllowAny
from .pagination import BoardPageNumberPagination


class ImageViewSet(viewsets.ModelViewSet):
    """ Board의 이미지 업로드 """
    queryset = models.Image.objects.all()
    serializer_class = serializers.ImageSerializer


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
        alread_liked = board.like.filter(
            username=request.user.username).exists()

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
    queryset = models.Session.objects.all()
    serializer_class = serializers.LectureSerializer
    action_serializer_classes = {
        "assignment": serializers.AssignmentSerializer, "add_assignment": serializers.AssignmentSerializer}
    filter_class = filters.SessionFilter
    pagination_class = BoardPageNumberPagination
    category = "session"
    # permission_classes =( IsStaffOrReadonly,)

    def get_queryset(self, session_type=models.Session.LECTURE):
        query = super().get_queryset()
        query = query.filter(session_type=session_type)
        return query

    def get_object(self):
        queryset = models.Session.objects.all()
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

    @action(detail=False, methods=['GET'], url_path='assignment/(?P<assignment_id>[^/.]+)')
    def assignment(self, request, assignment_id, *args, **kwargs):
        queryset = self.get_queryset(models.Session.ASSIGNMENT)
        queryset = get_object_or_404(queryset, pk=assignment_id)
        serializer = self.get_serializer(data=[queryset], many=True)
        serializer.is_valid()
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def add_assignment(self, request, *args, **kwargs):
        session = self.get_object()
        assignment = session.add_assignment(**request.data)

        serializer = self.get_serializer(data=assignment)
        if session.session_type == session.ASSIGNMENT:
            print(session.session_type)
            raise rest_framework.serializers.ValidationError(
                "ASSIGNMENT Type Session must not have assignment")
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class SubmissionViewSet(BaseBoardViewSet):
    queryset = models.Submission.objects.all()
    serializer_class = serializers.SubmissionSerializer
    action_serializer_classes = {
        "evaluation": serializers.SubmissionEvaluateSerializer}
    filter_class = filters.SubmissionFilter
    category = "submission"

    @action(detail=True, methods=['POST'])
    def evaluation(self, request, *args, **kwargs):
        '''
        제출된 과제에 대해 점수를 메기고 코멘트를 남기는 API

        ---
        ## `/board/submission/<int:pk>/evaluation/`
        ## 내용
            - score_info: {
                "평가요소": 점수
                ...
            }
            - evaluation_info: {
                "evaluator": user_pk
                "evaluation": "과제에 대한 코멘트"
            }
        '''
        score_dict_list = request.data.get("score_info")
        evaluation_info = request.data.get("evaluation_info")

        submission = self.get_object()
        submission.evaluate(score_dict_list, evaluation_info)
        serializer = self.get_serializer(data=[submission], many=True)
        serializer.is_valid()
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)


class StudyViewSet(BaseBoardViewSet):
    queryset = models.StudyBoard.objects.all()
    serializer_class = serializers.StudyBoardSerializer
    filter_class = filters.StudyBoardFilter
    category = "study"
    pagination_class = BoardPageNumberPagination
    # permission_classes =(IsStudyMemberOrReadonly,)


# 공지 게시판 viewset
class NoticeViewSet(BaseBoardViewSet):
    queryset = models.NoticeBoard.objects.all()
    serializer_class = serializers.NoticeBoardSerializer
    filter_class = filters.NoticeBoardFilter
    category = "notice"
    pagination_class = BoardPageNumberPagination

    # permission_classes =( IsStaffOrReadonly,)


# QnA 게시판 viewset
class QnAViewSet(BaseBoardViewSet):
    queryset = models.QnABoard.objects.all()
    serializer_class = serializers.QnABoardSerializer
    filter_class = filters.QnABoardFilter
    category = "qna"
    pagination_class = BoardPageNumberPagination
    # custom permission 예시들
    # 지우지 말아주세요!!!
    # permission_classes=[AllowAny]

    # def get_permissions(self):
    #     print(self.action)
    #     if self.action in ['retrieve']:
    #         return [IsAuthorOrReadonly(), ]
    #     return [permission() for permission in self.permission_classes]


class CareerViewSet(BaseBoardViewSet):
    queryset = models.CareerBoard.objects.all()
    serializer_class = serializers.CareerBoardSerializer
    filter_class = filters.CareerBoardFilter
    category = "career"
    pagination_class = BoardPageNumberPagination


class SessionCommentViewSet(viewsets.ModelViewSet):
    queryset = models.SessionComment.objects.all()
    serializer_class = serializers.SessionCommentSerializer


class SubmissionCommentViewSet(viewsets.ModelViewSet):
    queryset = models.SubmissionComment.objects.all()
    serializer_class = serializers.SubmissionCommentSerializer


# 스터디 댓글 viewset
class StudyCommentViewSet(viewsets.ModelViewSet):
    queryset = models.StudyBoardComment.objects.all()
    serializer_class = serializers.StudyBoardCommentSerializer
    filter_class = filters.StudyBoardCommentFilter


# 공지 댓글 viewset
class NoticeCommentViewSet(viewsets.ModelViewSet):
    queryset = models.NoticeBoardComment.objects.all()
    serializer_class = serializers.NoticeBoardCommentSerializer
    filter_class = filters.NoticeBoardCommentFilter


# QnA 댓글 viewset
class QnACommentViewSet(viewsets.ModelViewSet):
    queryset = models.QnABoardComment.objects.all()
    serializer_class = serializers.QnABoardCommentSerializer
    filter_class = filters.QnABoardCommentFilter

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(is_child=False)
        return query

    def get_object(self):
        queryset = models.QnABoardComment.objects.all()
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
        print("데이터:   ", request.data)
        print("new_comment_dict:  ", new_comment_dict)

        serializer = self.get_serializer(data=new_comment_dict)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
