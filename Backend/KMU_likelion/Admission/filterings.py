import django_filters
from .models import *
from django_filters import filters

class JoinFormFilter(django_filters.rest_framework.FilterSet):
    
    class Meta:
        model = JoinForm
        fields='__all__'

class QuestionFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Question
        fields='__all__'

class AnswerFilter(django_filters.rest_framework.FilterSet):
    joinform = filters.NumberFilter(field_name="joinform_id__id")
    question = filters.NumberFilter(field_name="question_id__id")
    class Meta:
        model = Answer
        fields='__all__'

class EvaluationFilter(django_filters.rest_framework.FilterSet):
    joinform_id = filters.NumberFilter(field_name="joinform_id__id")
    user_id = filters.NumberFilter(field_name="user_id__id")
    class Meta:
        model = Evaluation
        fields='__all__'


