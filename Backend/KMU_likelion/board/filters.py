import django_filters
from django_filters import filters

from . import models


class SessionFilter(django_filters.rest_framework.FilterSet):
    user_id = filters.NumberFilter(field_name="user_id__id")

    class Meta:
        model = models.Session
        fields = '__all__'


class SubmissionFilter(django_filters.rest_framework.FilterSet):
    user_id = filters.NumberFilter(field_name="user_id__id")

    class Meta:
        model = models.Submission
        fields = '__all__'


class StudyBoardFilter(django_filters.rest_framework.FilterSet):
    group_id = filters.NumberFilter(field_name="group_id__id")
    user_id = filters.NumberFilter(field_name="user_id__id")

    class Meta:
        model = models.StudyBoard
        fields = '__all__'


class NoticeBoardFilter(django_filters.rest_framework.FilterSet):
    user_id = filters.NumberFilter(field_name="user_id__id")

    class Meta:
        model = models.NoticeBoard
        fields = '__all__'


class QnABoardFilter(django_filters.rest_framework.FilterSet):
    user_id = filters.NumberFilter(field_name="user_id__id")

    class Meta:
        model = models.QnABoard
        fields = '__all__'


class CareerBoardFilter(django_filters.rest_framework.FilterSet):
    user_id = filters.NumberFilter(field_name="user_id__id")

    class Meta:
        model = models.CareerBoard
        fields = '__all__'


class StudyBoardCommentFilter(django_filters.rest_framework.FilterSet):
    user_id = filters.NumberFilter(field_name="user_id__id")
    board_id = filters.NumberFilter(field_name="board__id")

    class Meta:
        model = models.StudyBoardComment
        fields = '__all__'


class NoticeBoardCommentFilter(django_filters.rest_framework.FilterSet):
    user_id = filters.NumberFilter(field_name="user_id__id")
    board_id = filters.NumberFilter(field_name="board__id")

    class Meta:
        model = models.NoticeBoardComment
        fields = '__all__'


class QnABoardCommentFilter(django_filters.rest_framework.FilterSet):
    user_id = filters.NumberFilter(field_name="user_id__id")
    board_id = filters.NumberFilter(field_name="board__id")

    class Meta:
        model = models.QnABoardComment
        fields = '__all__'
