# api/views.py
from django.contrib.auth import get_user_model
from knox.models import AuthToken
from rest_framework import generics, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .filters import (GroupUserFilter, MentoringFilter, PortfolioFilter,
                      StudyGroupFilter, UserFilter)
from .models import GroupUser, Mentoring, Portfolio, StudyGroup
from .serializers import (CreateUserSerializer, GroupUserCreateSerializer,
                          GroupUserSerializer, LoginUserSerializer,
                          MenteeSerializer, MentoringSerializer,
                          MentorSerializer, PortfolioSerializer,
                          StudyGroupSerializer, UserActivitySerializer,
                          UserSerializer)

User = get_user_model()
import json

class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        if len(request.data["email"]) < 6 or len(request.data["password"]) < 4:
            body = {"message": "short field"}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"user": UserSerializer(user, context=self.get_serializer_context()).data,
                         "token": AuthToken.objects.create(user)[1], })


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({"user": UserSerializer(user, context=self.get_serializer_context()).data,
                         "token": AuthToken.objects.create(user)[1], })


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    action_serializer_classes = {"activity": UserActivitySerializer}
    filter_class = UserFilter

    def get_serializer_class(self):
        return self.action_serializer_classes.get(self.action, self.serializer_class)

    @action(detail=True, methods=["GET"])
    def activity(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    @action(detail=True, methods=["GET"])
    def get_mymentees(self, request, *args, **kwargs):
        mentor = self.get_object()
        mentees = Mentoring.objects.filter(mentor=mentor.id)
        serializer = MenteeSerializer(mentees, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["GET"])
    def get_mymentors(self, request, *args, **kwargs):
        mentee = self.get_object()
        mentors = Mentoring.objects.filter(mentee=mentee.id)
        serializer = MentorSerializer(mentors, many=True)
        return Response(serializer.data)
    
    @action(detail = False, methods=["POST"])
    def delete_mentoring(self, request, *args, **kwargs):
        json_mentoring = request.body
        mentoring = json.loads(json_mentoring)
        mentor = mentoring['mentor_id']
        mentee = mentoring['mentee_id']
        try:
            obj_mentoring = Mentoring.objects.get(mentor=mentor,mentee = mentee)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        obj_mentoring.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class StudyGroupViewSet(viewsets.ModelViewSet):
    queryset = StudyGroup.objects.all().order_by('pub_date')
    serializer_class = StudyGroupSerializer
    filter_class = StudyGroupFilter

    @action(detail=True, methods=["GET"])
    def group_users(self, request, *args, **kwargs):
        group = self.get_object()
        group_users = group.groupuser_set.all()
        serializer = GroupUserSerializer(group_users, many=True)
        return Response(serializer.data)


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    filter_class = PortfolioFilter


class GroupUserViewSet(viewsets.ModelViewSet):
    queryset = GroupUser.objects.all()
    serializer_class = GroupUserCreateSerializer
    filter_class = GroupUserFilter


class MentoringViewSet(viewsets.ModelViewSet):
    queryset = Mentoring.objects.all()
    serializer_class = MentoringSerializer
    filter_class = MentoringFilter

    @action(detail=False, methods=["GET"])
    def get_mentors(self, request, *args, **kwargs):
        queryset = Mentoring.objects.exclude(mentor=None)
        querylist = []
        # 중복제거
        for qs in queryset:
            flags = False
            if not querylist:
                querylist.append(qs)
                flags = True
            else:
                for query in querylist:
                    if query.mentor.id == qs.mentor.id:
                        flags = True
            if not flags:
                querylist.append(qs)

        serializer = MentorSerializer(querylist, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["GET"])
    def get_mentees(self, request, *args, **kwargs):
        queryset = Mentoring.objects.exclude(mentee=None)
        querylist = []
        # 중복제거
        for qs in queryset:
            flags = False
            if not querylist:
                querylist.append(qs)
                flags = True
            else:
                for query in querylist:
                    if query.mentee.id == qs.mentee.id:
                        flags = True
            if not flags:
                querylist.append(qs)

        serializer = MenteeSerializer(querylist, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        check = serializer.validated_data
        mentoring_log = Mentoring.objects.filter(mentor=check['mentor'].id)
        for mentor in mentoring_log:
            if mentor.mentee.id == check['mentee'].id:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
