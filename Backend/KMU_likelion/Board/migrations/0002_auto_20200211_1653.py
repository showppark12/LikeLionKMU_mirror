# Generated by Django 3.0.2 on 2020-02-11 07:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Board', '0001_initial'),
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='studycomments',
            name='user_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='studyboard',
            name='group_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='group_board', to='accounts.StudyGroup'),
        ),
        migrations.AddField(
            model_name='studyboard',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='study_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='studyboard',
            name='user_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='recruitcomments',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recruit_comments', to='Board.RecruitBoard'),
        ),
        migrations.AddField(
            model_name='recruitcomments',
            name='user_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='recruitboard',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='recruit_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='recruitboard',
            name='user_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='qnacomments',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='QnA_comments', to='Board.QnABoard'),
        ),
        migrations.AddField(
            model_name='qnacomments',
            name='user_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='qnaboard',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='qna_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='qnaboard',
            name='user_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='noticecomments',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notice_comments', to='Board.NoticeBoard'),
        ),
        migrations.AddField(
            model_name='noticecomments',
            name='user_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='noticeboard',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='notice_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='noticeboard',
            name='user_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
