# Generated by Django 3.0.2 on 2020-02-07 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hashtag',
            name='Tag',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
