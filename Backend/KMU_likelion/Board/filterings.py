import django_filters
from .models import *
from django_filters import filters

class StudyFilter(django_filters.rest_framework.FilterSet):
    group_id = filters.NumberFilter(field_name="group_id__id")
    user_id = filters.NumberFilter(field_name="user_id__id")
    class Meta:
        model = StudyBoard
        fields='__all__'

class NoticeFilter(django_filters.rest_framework.FilterSet):
    user_id = filters.NumberFilter(field_name="user_id__id")
    class Meta:
        model = NoticeBoard
        fields='__all__'

class QnAFilter(django_filters.rest_framework.FilterSet):
    user_id = filters.NumberFilter(field_name="user_id__id")
    class Meta:
        model = QnABoard
        fields = '__all__'

class RecruitFilter(django_filters.rest_framework.FilterSet):
    user_id = filters.NumberFilter(field_name="user_id__id")
    class Meta:
        model = RecruitBoard
        fields = '__all__'

class StudyCommentFilter(django_filters.rest_framework.FilterSet):
    user_id = filters.NumberFilter(field_name="user_id__id")
    board_id = filters.NumberFilter(field_name="board__id")
    class Meta:
        model = StudyComments
        fields = '__all__'

class NoticeCommentFilter(django_filters.rest_framework.FilterSet):
    user_id = filters.NumberFilter(field_name="user_id__id")
    board_id = filters.NumberFilter(field_name="board__id")
    class Meta:
        model = NoticeComments
        fields = '__all__'

class QnACommentFilter(django_filters.rest_framework.FilterSet):
    user_id = filters.NumberFilter(field_name="user_id__id")
    board_id = filters.NumberFilter(field_name="board__id")
    class Meta:
        model = QnAComments
        fields = '__all__'

class RecruitCommentFilter(django_filters.rest_framework.FilterSet):
    user_id = filters.NumberFilter(field_name="user_id__id")
    board_id = filters.NumberFilter(field_name="board__id")
    class Meta:
        model = RecruitComments
        fields = '__all__'