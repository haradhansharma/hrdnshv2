# Generated by Django 4.0.6 on 2023-09-23 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('literature', '0003_alter_story_story_outline_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storyraw',
            name='title',
        ),
    ]
