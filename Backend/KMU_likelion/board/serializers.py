from rest_framework import serializers

from .models import (CareerBoard, NoticeBoard, NoticeBoardComment, QnABoard,
                     QnABoardComment, Score, Session, StudyBoard,
                     StudyBoardComment, Submission)


# Session type=ASSIGNMENT Serializer
class AssignmentSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='user_id.username')
    session_type = serializers.HiddenField(default='A')

    class Meta:
        model = Session
        fields = ['id', 'author_name', 'title', 'user_id', 'body', 'score_types',
                  'pub_date', 'update_date', 'session_type', 'lecture']


# Session type=LECTURE Serializer
class LectureSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='user_id.username')
    assignments = AssignmentSerializer(many=True)

    class Meta:
        model = Session
        fields = ['id', 'author_name', 'title', 'body', 'user_id',
                  'pub_date', 'update_date', 'session_type', 'assignments']


class ScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Score
        fields = '__all__'


# 과제 제출 Serializer
class SubmissionSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='user_id.username')
    scores = ScoreSerializer(many=True, read_only=True)
    total_score = serializers.SerializerMethodField()

    class Meta:
        model = Submission
        fields = ['id', 'author_name', 'title', 'user_id', 'body', 'pub_date',
                  'update_date', 'lecture', 'scores', 'total_score']

    def create(self, validated_data):
        submission = super(SubmissionSerializer, self).create(validated_data)
        if not submission.add_scores_by_types():
            serializers.ValidationError(
                "Score_types field of submission's session object is null or blank")
        return submission

    def total_score(self):
        submission = self.get_object()
        return submission.total_score()


# 스터디 게시판 Serializer
class StudyBoardSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='user_id.username')
    group_name = serializers.ReadOnlyField(source='group_id.name')

    class Meta:
        model = StudyBoard
        fields = ['id', 'author_name', 'body', 'user_id', 'title', 'pub_date', 'update_date',
                  'like', 'total_likes', 'study_type', 'personnel', 'group_name', 'group_id']


# 공지 게시판 Serializer
class NoticeBoardSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='user_id.username')

    class Meta:
        model = NoticeBoard
        fields = ['id', 'author_name', 'body', 'user_id', 'title', 'pub_date',
                  'update_date', 'like', 'total_likes', 'notice_date', 'is_recorded', 'event_name']


# QnA 게시판 Serializer
class QnABoardSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='user_id.username')

    class Meta:
        model = QnABoard
        fields = ['id', 'author_name', 'body', 'user_id', 'title',
                  'subject', 'pub_date', 'update_date', 'like', 'total_likes']


class CareerBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerBoard
        fields = '__all__'


# 스터디 댓글 Serializer
class StudyBoardCommentSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='user_id.username')
    user_img = serializers.ImageField(
        source='user_id.img', read_only=True, use_url=True)

    class Meta:
        model = StudyBoardComment
        fields = ['id', 'author_name', 'body', 'user_id',
                  'board', 'pub_date', 'update_date', 'user_img']


# 공지 댓글 Serializer
class NoticeBoardCommentSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='user_id.username')
    user_img = serializers.ImageField(
        source='user_id.img', read_only=True, use_url=True)

    class Meta:
        model = NoticeBoardComment
        fields = ['id', 'author_name', 'body', 'user_id',
                  'board', 'pub_date', 'update_date', 'user_img']


# QnA 댓글 Serializer
class RecommentSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='user_id.username')
    user_img = serializers.ImageField(
        source='user_id.img', read_only=True, use_url=True)

    class Meta:
        model = QnABoardComment
        fields = ['id', 'author_name', 'body', 'user_id', 'board',
                  'pub_date', 'update_date', 'user_img', 'parent_id', 'is_child']


class QnABoardCommentSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='user_id.username')
    user_img = serializers.ImageField(
        source='user_id.img', read_only=True, use_url=True)
    recomments = RecommentSerializer(
        many=True, source='recomment', read_only=True)

    class Meta:
        model = QnABoardComment
        fields = ['id', 'author_name', 'body', 'user_id', 'board', 'pub_date',
                  'update_date', 'user_img', 'parent_id', 'is_child', 'recomments']
