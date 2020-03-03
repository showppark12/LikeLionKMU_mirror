from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers

from board import serializers as board_serializers
from board.serializer_fields import Base64ImageField
from .models import GroupUser, Mentoring, Portfolio, StudyGroup

User = get_user_model()


# 회원가입
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ["username","password", "first_name","last_name","email","major","is_staff","is_active","student_id","user_type","start_number","sns_id",
        "is_superuser" ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],password= validated_data["password"],first_name=validated_data["first_name"],
            last_name=validated_data["last_name"], email=validated_data["email"], is_staff=validated_data["is_staff"], is_active=validated_data["is_active"],
            is_superuser=validated_data["is_superuser"],major=validated_data["major"],student_id=validated_data["student_id"],
            user_type=validated_data["user_type"], start_number=validated_data["start_number"], sns_id=validated_data["sns_id"])
        return user


# 접속 유지중인지 확인
class UserSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(use_url = True , max_length = None)
    class Meta:
        model = User
        fields =  ["username", "first_name", "img", "id","email","major","student_id","user_type","start_number","sns_id" ]


# 유저의 활동 내역(글, 댓글)을 포함
class UserActivitySerializer(serializers.ModelSerializer):
    studyboard = board_serializers.StudyBoardSerializer(
        many=True, source="studyboard_set")
    noticeboard = board_serializers.NoticeBoardSerializer(
        many=True, source="noticeboard_set")
    qnaboard = board_serializers.QnABoardSerializer(
        many=True, source="qnaboard_set")
    assignments = board_serializers.AssignmentSerializer(
        many=True, source="session_set")
    submission = board_serializers.SubmissionSerializer(
        many=True, source="submission_set")

    studyboard_comments = board_serializers.StudyBoardCommentSerializer(
        many=True, source="studyboardcomment_set")
    noticeboard_comments = board_serializers.NoticeBoardCommentSerializer(
        many=True, source="noticeboardcomment_set")
    qnaboard_comments = board_serializers.QnABoardCommentSerializer(
        many=True, source="qnaboardcomment_set")
    sessionboard_comments = board_serializers.SessionCommentSerializer(
        many=True, source="sessioncomment_set")
    submissionboard_comments = board_serializers.SubmissionCommentSerializer(
        many=True, source="submissioncomment_set")

    class Meta:
        model = User
        fields = ["studyboard", "noticeboard", "qnaboard", "assignments", "submission", "studyboard_comments",
                  "noticeboard_comments", "qnaboard_comments", "sessionboard_comments", "submissionboard_comments"]


# 로그인
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError(
            "Unable to log in with provided credentials.")


class StudyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyGroup
        fields = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'


class GroupUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupUser
        fields = '__all__'


class GroupUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='user_id', read_only=True)

    class Meta:
        model = GroupUser
        fields = '__all__'


class MentoringSerializer(serializers.ModelSerializer):
    mentor_name = serializers.ReadOnlyField(source='mentor.username')
    mentee_name = serializers.ReadOnlyField(source='mentee.username')

    class Meta:
        model = Mentoring
        fields = ['id', 'pub_date', 'mentor',
                  'mentee', 'mentor_name', 'mentee_name']


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


class MyGroupSerializer(serializers.ModelSerializer):
    studygroup = StudyGroupSerializer(source='group_id')

    class Meta:
        model = GroupUser
        fields = ['studygroup', 'is_captain']


class CaptainSerializer(serializers.ModelSerializer):
    user_img = serializers.ImageField(
        source='user_id.img', read_only=True, use_url=True)
    captain_username = serializers.ReadOnlyField(source='user_id.username')

    class Meta:
        model = GroupUser
        fields = ['user_img', 'captain_username', 'user_id', 'full_name']
