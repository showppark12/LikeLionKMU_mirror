import django_filters
from django_filters import filters

from .models import (CareerBoard, NoticeBoard, NoticeBoardComment, QnABoard,
                     QnABoardComment, StudyBoard, StudyBoardComment)


class StudyBoardFilter(django_filters.rest_framework.FilterSet):
    group_id = filters.NumberFilter(field_name="group_id__id")
    user_id = filters.NumberFilter(field_name="user_id__id")

    class Meta:
        model = StudyBoard
        fields = '__all__'


class NoticeBoardFilter(django_filters.rest_framework.FilterSet):
    user_id = filters.NumberFilter(field_name="user_id__id")

    class Meta:
        model = NoticeBoard
        fields = '__all__'


class QnABoardFilter(django_filters.rest_framework.FilterSet):
    user_id = filters.NumberFilter(field_name="user_id__id")

    class Meta:
        model = QnABoard
        fields = '__all__'


class CareerBoardFilter(django_filters.rest_framework.FilterSet):
    user_id = filters.NumberFilter(field_name="user_id__id")

    class Meta:
        model = CareerBoard
        fields = '__all__'


class StudyBoardCommentFilter(django_filters.rest_framework.FilterSet):
    user_id = filters.NumberFilter(field_name="user_id__id")
    board_id = filters.NumberFilter(field_name="board__id")

    class Meta:
        model = StudyBoardComment
        fields = '__all__'


class NoticeBoardCommentFilter(django_filters.rest_framework.FilterSet):
    user_id = filters.NumberFilter(field_name="user_id__id")
    board_id = filters.NumberFilter(field_name="board__id")

    class Meta:
        model = NoticeBoardComment
        fields = '__all__'


class QnABoardCommentFilter(django_filters.rest_framework.FilterSet):
    user_id = filters.NumberFilter(field_name="user_id__id")
    board_id = filters.NumberFilter(field_name="board__id")

    class Meta:
        model = QnABoardComment
        fields = '__all__'
