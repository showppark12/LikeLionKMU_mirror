# api/views.py
from rest_framework import viewsets, permissions, generics, status
from django.contrib.auth.signals import user_logged_in, user_logged_out
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action, api_view
from knox.models import AuthToken
from knox.auth import TokenAuthentication
from .serializers import *
from .models import *
from .filterings import *


class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        if len(request.data["email"]) < 6 or len(request.data["password"]) < 4:
            body = {"message": "short field"}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"user": UserSerializer(user, context=self.get_serializer_context()).data, "token": AuthToken.objects.create(user)[1], })


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({"user": UserSerializer(user, context=self.get_serializer_context()).data, "token": AuthToken.objects.create(user)[1], })


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


class StudyGroupViewSet(viewsets.ModelViewSet):
    queryset = StudyGroup.objects.all().order_by('pub_date')
    serializer_class = StudyGroupSerializer
    filter_class = StudyGroupFilter


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    filter_class = PortfolioFilter


class GroupUserViewSet(viewsets.ModelViewSet):
    queryset = GroupUser.objects.all()
    serializer_class = GroupUserSerializer
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
            if flags == False:
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
            if flags == False:
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
