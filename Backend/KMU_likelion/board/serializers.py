from rest_framework import serializers

from . import models, serializer_fields


class ImageSerializer(serializers.ModelSerializer):
    image = serializer_fields.Base64ImageField()

    class Meta:
        model = models.Image
        fields = ['image']


# Session type=ASSIGNMENT Serializer
class AssignmentSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='user_id.username')
    session_type = serializers.HiddenField(default='A')
    deadline = serializers.DateTimeField(required=False)

    class Meta:
        model = models.Session
        fields = ['id', 'author_name', 'title', 'user_id', 'body', 'score_types',
                  'pub_date', 'update_date', 'session_type', 'lecture', 'deadline']  # 'deadline'


# Session type=LECTURE Serializer
class LectureSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='user_id.username')
    assignments = AssignmentSerializer(many=True, read_only=True)

    class Meta:
        model = models.Session
        fields = ['id', 'author_name', 'full_name', 'title', 'body', 'user_id',
                  'pub_date', 'update_date', 'session_type', 'assignments', 'start_number']


class ScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Score
        fields = '__all__'


class SubmissionSerializer(serializers.ModelSerializer):
    """ 과제 제출 """
    author_name = serializers.ReadOnlyField(source='user_id.username')
    scores = ScoreSerializer(many=True, read_only=True)
    total_score = serializers.SerializerMethodField()

    evaluator_name = serializers.ReadOnlyField(source='evaluator.username')

    class Meta:
        model = models.Submission
        fields = ['id', 'author_name', 'full_name', 'title', 'user_id', 'body', 'pub_date',
                  'update_date', 'lecture', 'scores', 'total_score', 'url',
                  'evaluator', 'evaluator_name', 'evaluation', 'evaluation_pub_date', 'evaluation_update_date']
        read_only_fields = ('evaluator', 'evaluation',
                            'evaluation_pub_date', 'evaluation_update_date',)

    def create(self, validated_data):
        submission = super(SubmissionSerializer, self).create(validated_data)
        if not submission.add_scores_by_types():
            serializers.ValidationError(
                "Score_types field of submission's session object is null or blank")
        return submission

    def total_score(self):
        submission = self.get_object()
        return submission.total_score()


class SubmissionEvaluateSerializer(serializers.ModelSerializer):
    """ 과제 평가 """

    class Meta:
        model = models.Submission
        fields = ['id', 'evaluator', 'evaluation', ]


# 스터디 게시판 Serializer
class StudyBoardSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='user_id.username')
    group_name = serializers.ReadOnlyField(source='group_id.name')

    class Meta:
        model = models.StudyBoard
        fields = ['id', 'author_name', 'body', 'user_id', 'full_name', 'title', 'pub_date', 'update_date',
                  'like', 'total_likes', 'study_type', 'personnel', 'group_name', 'group_id']


# 공지 게시판 Serializer
class NoticeBoardSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='user_id.username')

    class Meta:
        model = models.NoticeBoard
        fields = ['id', 'author_name', 'full_name', 'body', 'user_id', 'title', 'pub_date',
                  'update_date', 'like', 'total_likes', 'notice_date', 'is_recorded', 'event_name']


# QnA 게시판 Serializer
class QnABoardSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='user_id.username')

    class Meta:
        model = models.QnABoard
        fields = ['id', 'author_name', 'full_name', 'body', 'user_id', 'title',
                  'subject', 'pub_date', 'update_date', 'like', 'total_likes']


class CareerBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CareerBoard
        fields = '__all__'


class SessionCommentSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='user_id.username')
    user_img = serializers.ImageField(
        source='user_id.img', read_only=True, use_url=True)

    class Meta:
        model = models.SessionComment
        fields = ['id', 'author_name', 'full_name', 'body', 'user_id',
                  'board', 'pub_date', 'update_date', 'user_img']


class SubmissionCommentSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='user_id.username')
    user_img = serializers.ImageField(
        source='user_id.img', read_only=True, use_url=True)

    class Meta:
        model = models.SubmissionComment
        fields = ['id', 'author_name', 'full_name', 'body', 'user_id',
                  'board', 'pub_date', 'update_date', 'user_img', 'is_grader']


# 스터디 댓글 Serializer
class StudyBoardCommentSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='user_id.username')
    user_img = serializers.ImageField(
        source='user_id.img', read_only=True, use_url=True)

    class Meta:
        model = models.StudyBoardComment
        fields = ['id', 'author_name', 'full_name', 'body', 'user_id',
                  'board', 'pub_date', 'update_date', 'user_img']


# 공지 댓글 Serializer
class NoticeBoardCommentSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='user_id.username')
    user_img = serializers.ImageField(
        source='user_id.img', read_only=True, use_url=True)

    class Meta:
        model = models.NoticeBoardComment
        fields = ['id', 'author_name', 'full_name', 'body', 'user_id',
                  'board', 'pub_date', 'update_date', 'user_img']


# QnA 댓글 Serializer
class RecommentSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='user_id.username')
    user_img = serializers.ImageField(
        source='user_id.img', read_only=True, use_url=True)

    class Meta:
        model = models.QnABoardComment
        fields = ['id', 'author_name', 'full_name', 'body', 'user_id', 'board',
                  'pub_date', 'update_date', 'user_img', 'parent_id', 'is_child']


class QnABoardCommentSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='user_id.username')
    user_img = serializers.ImageField(
        source='user_id.img', read_only=True, use_url=True)
    recomments = serializer_fields.RecursiveSerializer(
        many=True, read_only=True)

    class Meta:
        model = models.QnABoardComment
        fields = ['id', 'author_name', 'full_name', 'body', 'user_id', 'board', 'pub_date',
                  'update_date', 'user_img', 'parent_id', 'is_child', 'recomments']
