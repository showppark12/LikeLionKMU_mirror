import django_filters
from django_filters import filters

from .models import (NoticeBoard, NoticeComment, QnABoard, QnAComment,
                     StudyBoard, StudyComment)


class StudyFilter(django_filters.rest_framework.FilterSet):
    group_id = filters.NumberFilter(field_name="group_id__id")
    user_id = filters.NumberFilter(field_name="user_id__id")

    class Meta:
        model = StudyBoard
        fields = '__all__'


class NoticeFilter(django_filters.rest_framework.FilterSet):
    user_id = filters.NumberFilter(field_name="user_id__id")

    class Meta:
        model = NoticeBoard
        fields = '__all__'


class QnAFilter(django_filters.rest_framework.FilterSet):
    user_id = filters.NumberFilter(field_name="user_id__id")

    class Meta:
        model = QnABoard
        fields = '__all__'


class StudyCommentFilter(django_filters.rest_framework.FilterSet):
    user_id = filters.NumberFilter(field_name="user_id__id")
    board_id = filters.NumberFilter(field_name="board__id")

    class Meta:
        model = StudyComment
        fields = '__all__'


class NoticeCommentFilter(django_filters.rest_framework.FilterSet):
    user_id = filters.NumberFilter(field_name="user_id__id")
    board_id = filters.NumberFilter(field_name="board__id")

    class Meta:
        model = NoticeComment
        fields = '__all__'


class QnACommentFilter(django_filters.rest_framework.FilterSet):
    user_id = filters.NumberFilter(field_name="user_id__id")
    board_id = filters.NumberFilter(field_name="board__id")

    class Meta:
        model = QnAComment
        fields = '__all__'
