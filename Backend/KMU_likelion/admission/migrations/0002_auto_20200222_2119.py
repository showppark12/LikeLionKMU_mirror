# Generated by Django 3.0.2 on 2020-02-22 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('R', '심사중'), ('F', '불합격'), ('P', '합격')], default='R', max_length=1),
        ),
    ]