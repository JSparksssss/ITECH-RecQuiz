# Generated by Django 2.1.5 on 2022-03-06 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecQuiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
