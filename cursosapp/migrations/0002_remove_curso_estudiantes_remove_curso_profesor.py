# Generated by Django 5.0.7 on 2024-07-29 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursosapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='estudiantes',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='profesor',
        ),
    ]
