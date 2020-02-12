# api/views.py
from rest_framework import viewsets, permissions, generics, status
from django.contrib.auth.signals import user_logged_in, user_logged_out
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from knox.models import AuthToken
from knox.auth import TokenAuthentication
from .serializers import *
from .models import *



# Create your views here.
# @api_view(["GET"])
# def HelloAPI(request):
#     return Response("hello world!")


class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        if len(request.data["username"]) < 6 or len(request.data["password"]) < 4:
            body = {"message": "short field"}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StudyGroupViewSet(viewsets.ModelViewSet):
    queryset = StudyGroup.objects.all().order_by('pub_date')
    serializer_class = StudyGroupSerializer
    def get_queryset(self):
        qs=super().get_queryset()
        group_name=self.request.query_params.get('group_name','')
        if group_name:
            qs = qs.filter(name=group_name)
        return qs

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset =Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class Group_UserViewSet(viewsets.ModelViewSet):
    queryset =Group_User.objects.all()
    serializer_class = Group_UserSerializer
    