# Generated by Django 4.0.6 on 2023-09-24 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('literature', '0010_alter_story_sigment_story_alter_storyoutline_segment'),
    ]

    operations = [
        migrations.AddField(
            model_name='storyraw',
            name='title',
            field=models.CharField(blank=True, help_text='It an keep blank to add from response of chatGPT', max_length=200, null=True),
        ),
    ]
