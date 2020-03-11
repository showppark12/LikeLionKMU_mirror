# Generated by Django 3.0.2 on 2020-03-03 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0018_submissioncomment_is_grader'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='evaluation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='submission',
            name='evaluation_pub_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='submission',
            name='evaluation_update_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='submission',
            name='evaluator',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='evaluation_history', to=settings.AUTH_USER_MODEL),
        ),
    ]