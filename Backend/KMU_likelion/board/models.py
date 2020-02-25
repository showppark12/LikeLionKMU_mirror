import re

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Sum

from accounts.models import StudyGroup

User = get_user_model()


class AbstractBaseBoard(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)  # 게시물 등록 시간 생성
    update_date = models.DateTimeField(auto_now=True)  # 업데이트 될 때만 정보 바뀔때 마다
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    class Meta:
        abstract = True
        ordering = ['-pub_date', ]

    def __str__(self):
        return self.title
    def full_name(self):
        return self.user_id.get_full_name()


class Session(AbstractBaseBoard):
    LECTURE = 'L'
    ASSIGNMENT = 'A'
    TYPE = (
        (LECTURE, "강의자료"),
        (ASSIGNMENT, '과제')
    )
    session_type = models.CharField(max_length=1, choices=TYPE)
    deadline = models.DateTimeField(blank=True, null=True)  # 과제 기한
    score_types = models.CharField(max_length=255, blank=True, null=True)

    lecture = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.PROTECT, related_name='assignments')
    like = models.ManyToManyField(User, blank=True, related_name="session_like")

    def get_lectures(self):
        return Session.objects.filter(session_type=self.LECTURE)
    
    def get_assignments(self):
        return Session.objects.filter(session_type=self.ASSIGNMENT)

    def add_assignment(self, **kwargs):
        kwargs['lecture'] = self.id
        kwargs['session_type'] = self.ASSIGNMENT
        return kwargs


class Score(models.Model):
    score_type = models.CharField(max_length=10)
    score = models.PositiveIntegerField(default=0)

    def set_score(request, score_num):
        score = score_num


class Submission(AbstractBaseBoard):
    lecture = models.ForeignKey(Session, on_delete=models.CASCADE)
    scores = models.ManyToManyField(
        Score, blank=True, related_name="+", symmetrical=False)
    like = models.ManyToManyField(User, blank=True, related_name="submission_like")

    def add_scores_by_types(self):
        if self.lecture.score_types:
            score_type_list = re.split('\W+', self.lecture.score_types)
            score_obj_list = [Score.objects.create(score_type=t) for t in score_type_list]
            print(score_obj_list)
            self.scores.set(score_obj_list, clear=True)
            print(self.scores.all())
            return True
        return False

    def set_scores_by_types(self, type_score_dict):
        """
        TODO : 딕셔너리에 맞게 type: score 를 지정해주도록 
        """
        pass

    @property
    def total_score(self):
        return self.scores.aggregate(Sum('score')) or 0


class StudyBoard(AbstractBaseBoard):
    study_type = models.IntegerField(default=0)  # 0: 공식모임, 1: 정보공유 2: etc
    personnel = models.IntegerField(default=0)
    group_id = models.ForeignKey(
        StudyGroup, on_delete=models.CASCADE, related_name="group_board", default=None)
    like = models.ManyToManyField(User, blank=True, related_name="study_like")

    @property
    def total_likes(self):
        return self.like.count()


class NoticeBoard(AbstractBaseBoard):
    notice_date = models.DateField(null=True)
    is_recorded = models.BooleanField(default=False)  # 달력 기록여부
    event_name = models.CharField(
        max_length=20, blank=True, null=True)  # 달력에 표시될 이벤트의 이름
    like = models.ManyToManyField(User, blank=True, related_name="notice_like")

    @property
    def total_likes(self):
        return self.like.count()


class QnABoard(AbstractBaseBoard):
    subject = models.CharField(max_length=200)
    like = models.ManyToManyField(User, blank=True, related_name="qna_like")

    @property
    def total_likes(self):
        return self.like.count()


class CareerBoard(AbstractBaseBoard):
    link = models.URLField(blank=True)
    participants = models.ManyToManyField(
        User, blank=True, related_name="career_user")
    like = models.ManyToManyField(User, blank=True, related_name="carrer_like")


class AbstractBaseComment(models.Model):
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    class Meta:
        abstract = True
        ordering = ['-pub_date', ]

    def full_name(self):
        return self.user_id.get_full_name()


class SessionComment(AbstractBaseComment):
    board = models.ForeignKey(
        Session, on_delete=models.CASCADE, related_name="session_comments")


class SubmissionComment(AbstractBaseComment):
    board = models.ForeignKey(
        Submission, on_delete=models.CASCADE, related_name="session_comments")


class StudyBoardComment(AbstractBaseComment):
    board = models.ForeignKey(
        StudyBoard, on_delete=models.CASCADE, related_name="study_comments")


class NoticeBoardComment(AbstractBaseComment):
    board = models.ForeignKey(
        NoticeBoard, on_delete=models.CASCADE, related_name="notice_comments")


class QnABoardComment(AbstractBaseComment):
    board = models.ForeignKey(
        QnABoard, on_delete=models.CASCADE, related_name="qna_comments")
    parent_id = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="recomments")
    # false는 부모 댓글 true는 대댓글, 대대댓글은 안할꼬얌
    is_child = models.BooleanField(default=False)

    def re_comment(self, **kwargs):
        for key, value in kwargs.items():
            kwargs[key] = value[0]
        kwargs['parent_id'] = self.id
        kwargs['is_child'] = True
        return kwargs
