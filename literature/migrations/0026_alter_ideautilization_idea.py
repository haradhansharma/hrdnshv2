# Generated by Django 4.0.6 on 2023-09-27 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('literature', '0025_alter_storyraw_genre_alter_storyraw_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ideautilization',
            name='idea',
            field=models.TextField(help_text='The place is to describe ideas to get best parameters to write literature. Primarily system will suggest title, genre, type, main charecter, settings, conflict, tone, style, topic,purpose, audience, keypoints, theme, mood, species quest.', max_length=1500, verbose_name='Describe your idea in maximum 500 characters'),
        ),
    ]
