# Generated by Django 3.0.2 on 2020-02-13 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='img',
            field=models.ImageField(default='../static/images/default_profile_img.png', upload_to='images/'),
        ),
    ]
