# Generated by Django 3.0.2 on 2020-02-28 17:21

import board.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('board', '0011_auto_20200225_0310'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='session_file',
            field=models.FileField(blank=True, null=True, upload_to=board.models.get_file_path),
        ),
        migrations.CreateModel(
            name='GenericImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=board.models.get_file_path)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
    ]
