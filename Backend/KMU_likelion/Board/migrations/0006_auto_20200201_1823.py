# Generated by Django 2.2.7 on 2020-02-01 09:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Board', '0005_recuitboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='board',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='noticeboard',
            name='run_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
