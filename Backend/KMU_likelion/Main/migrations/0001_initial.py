# Generated by Django 2.2 on 2020-02-10 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Board', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('link', models.TextField()),
                ('participants', models.ManyToManyField(blank=True, related_name='career_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Calender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('contents', models.CharField(max_length=200)),
                ('plan_type', models.IntegerField(default=0)),
                ('notice_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='calender', to='Board.NoticeBoard')),
            ],
        ),
    ]
