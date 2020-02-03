# Generated by Django 2.2.7 on 2020-02-03 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Board', '0007_auto_20200203_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyComments',
            fields=[
                ('comments_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Board.Comments')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='study_comments', to='Board.StudyBoard')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('Board.comments',),
        ),
    ]
