# Generated by Django 3.0.2 on 2020-02-14 13:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Board', '0002_auto_20200214_2241'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='career_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='calendar',
            name='notice_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='calender', to='Board.NoticeBoard'),
        ),
    ]
