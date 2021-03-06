# Generated by Django 3.0.2 on 2020-02-24 17:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0009_auto_20200225_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='careerboard',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='carrer_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='session',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='session_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='submission',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='submission_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
