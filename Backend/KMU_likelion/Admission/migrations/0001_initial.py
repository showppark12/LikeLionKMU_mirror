# Generated by Django 3.0.2 on 2020-02-19 15:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=50, unique=True)),
                ('student_id', models.CharField(default=None, max_length=50)),
                ('birth', models.DateField()),
                ('sex', models.CharField(max_length=50, null=True)),
                ('major', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('pw', models.CharField(max_length=50, null=True)),
                ('status', models.CharField(choices=[('F', '불합격'), ('R', '심사중'), ('P', '합격')], default='R', max_length=1)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('score', models.FloatField(default=0.0)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('applicationform_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='application_evaluation', to='admission.Application')),
                ('user_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_evaluation', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
