import json

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .filters import (AnswerFilter, ApplicationFilter, EvaluationFilter,
                      QuestionFilter)
from .models import Answer, Application, Evaluation, Question
from .serializer import (AnswerSerializer, ApplicationSerializer,
                         EvaluationSerializer, QuestionSerializer)

# Create your views here.


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    filter_class = ApplicationFilter
    @action(detail=True)
    def count_score(self, request, *args, **kwargs):
        application = self.get_object()
        evaluations = application.application_evaluation.all()
        total_score = 0.0
        count = 0.0
        if not evaluations:
            return Response({'total_score': 0, 'average_score': 0})

        else:
            for evaluation in evaluations:
               total_score = total_score + evaluation.score
               count += 1
               average_score = total_score / count
            return Response({'total_score': total_score, 'average_score': average_score})

    @action(detail=False, methods=['POST'])
    def get_application(self, request, *args, **kwargs):
        json_application = request.body
        join = json.loads(json_application)
        email = join['email']
        password = join['password']
        print(email)
        try:
            application = Application.objects.get(email=email)
            answers = Answer.objects.filter(application_id=application.id)
            print(answers)
        except Application.DoesNotExist:
            return Response({'application': '이 이메일은 없는 이메일입니다.'}, status=status.HTTP_404_NOT_FOUND)

        if application.pw == password:
            serializer = ApplicationSerializer(application)
            answer_serializer = AnswerSerializer(answers, many=True)
            return Response({"join_forms": serializer.data, "answers": answer_serializer.data})

        else:
            return Response({'application': '잘못된 비밀번호 입니다.'}, status=status.HTTP_404_NOT_FOUND)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_class = QuestionFilter


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filter_class = AnswerFilter

    @action(detail=False, methods=['POST'])
    def post_answers(self, request, *args, **kwargs):
        json_datas = request.body
        datas = json.loads(json_datas)
        answer_list = datas['answers']
        join_id = datas['application_id']
        join_instance = Application.objects.get(id=join_id)
        for question_id, answer in answer_list.items():

            tmp = Answer()
            tmp.application_id = join_instance
            tmp.question_id = Question.objects.get(id=question_id)
            tmp.body = answer
            tmp.save()
        answers = Answer.objects.filter(application_id=join_id)
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)


class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
    filter_class = EvaluationFilter
