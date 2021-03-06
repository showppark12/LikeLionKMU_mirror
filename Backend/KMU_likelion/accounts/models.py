from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    major = models.CharField(max_length=200, null=True)
    student_id = models.CharField(max_length=200, null=True)
    user_type = models.IntegerField(null=True) #1: 회장, 2:운영진, 3:일반부원
    start_number = models.CharField(max_length=200, null=True)
    sns_id = models.CharField(max_length=200, null=True, blank=True)
    img = models.ImageField(upload_to='images/', default='../static/images/default_profile_img.png')

    def full_name(self):
        return self.get_full_name()


class Mentoring(models.Model):
    pub_date = models.DateField(auto_now_add=True)
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="mentor")
    mentee = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="mentee")


class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField()
    link = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_portfolio", default=None)


class StudyGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)
    pub_date = models.DateField(auto_now_add=True)
    introduction = models.TextField()
    img = models.ImageField(upload_to='images/', default='../static/images/defaut_group_image.png')


class GroupUser(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    group_id = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, null=True)
    is_captain = models.BooleanField(default=False)

    class Meta:
        unique_together = ("user_id", "group_id", )
        ordering = ("group_id", )
    def full_name(self):
        return self.user_id.get_full_name()
