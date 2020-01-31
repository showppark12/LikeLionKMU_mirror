# Generated by Django 3.0.2 on 2020-01-31 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyBoard',
            fields=[
                ('board_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Board.Board')),
                ('how_many_people', models.IntegerField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('Board.board',),
        ),
    ]
