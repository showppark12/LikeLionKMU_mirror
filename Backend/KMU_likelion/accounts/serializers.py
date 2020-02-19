from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers

from Board.serializers import (NoticeCommentSerializer, NoticeSerializer,
                               QnACommentSerializer, QnASerializer,
                               RecruitCommentSerializer, RecruitSerializer,
                               StudyCommentSerializer, StudySerializer)

from .models import GroupUser, Mentoring, Portfolio, StudyGroup

User = get_user_model()


# 회원가입
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data["email"], None, validated_data["password"])
        return user


# 접속 유지중인지 확인
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# 유저의 활동 내역(글, 댓글)을 포함
class UserActivitySerializer(serializers.ModelSerializer):
    studyboard = StudySerializer(many=True, source="studyboard_set")
    noticeboard = NoticeSerializer(many=True, source="noticeboard_set")
    qnaboard = QnASerializer(many=True, source="qnaboard_set")
    recruitboard = RecruitSerializer(many=True, source="recruitboard_set")

    studycomments = StudyCommentSerializer(many=True, source="studycomments_set")
    noticecomments = NoticeCommentSerializer(many=True, source="noticecomments_set")
    qnacomments = QnACommentSerializer(many=True, source="qnacomments_set")
    recruitcomments = RecruitCommentSerializer(many=True, source="recruitcomments_set")

    class Meta:
        model = User
        fields = ["studyboard", "noticeboard", "qnaboard", "recruitboard",
                  "studycomments", "noticecomments", "qnacomments", "recruitcomments"]


# 로그인
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")


class StudyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyGroup
        fields = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'


class GroupUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupUser
        fields = '__all__'


class MentoringSerializer(serializers.ModelSerializer):
    mentor_name = serializers.ReadOnlyField(source='mentor.username')
    mentee_name = serializers.ReadOnlyField(source='mentee.username')

    class Meta:
        model = Mentoring
        fields = ['id', 'pub_date', 'mentor', 'mentee', 'mentor_name', 'mentee_name']


class MentorSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='mentor')

    class Meta:
        model = Mentoring
        fields = ['user']


class MenteeSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='mentee')

    class Meta:
        model = Mentoring
        fields = ['user']
