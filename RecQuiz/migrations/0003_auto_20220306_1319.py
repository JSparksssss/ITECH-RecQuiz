# Generated by Django 2.1.5 on 2022-03-06 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecQuiz', '0002_auto_20220306_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
