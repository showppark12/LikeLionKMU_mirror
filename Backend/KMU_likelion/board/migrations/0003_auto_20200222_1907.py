# Generated by Django 3.0.2 on 2020-02-22 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20200222_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qnaboardcomment',
            name='parent_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recomment', to='board.QnABoardComment'),
        ),
    ]
