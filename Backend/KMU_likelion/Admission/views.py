from rest_framework import viewsets
from .models import *
from .serializer import *
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
# Create your views here.


class JoinFormViewSet(viewsets.ModelViewSet):
    queryset = JoinForm.objects.all()
    serializer_class = JoinFormSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_queryset(self):
        qs=super().get_queryset()
        joinform_id = self.request.query_params.get('joinform_id','')
        question_id = self.request.query_params.get('question_id','')
        if joinform_id:
            qs=qs.filter(joinform_id=joinform_id)
        elif question_id:
            qs=qs.filter(question_id = question_id)
        return qs

class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        joinform_id = self.request.query_params.get('joinform_id','')
        user_id = self.request.query_params.get('user_id','')
        if joinform_id:
            qs = qs.filter(joinform_id = joinform_id)
        elif user_id:
            qs = qs.filter(user_id = user_id)
        return qs




