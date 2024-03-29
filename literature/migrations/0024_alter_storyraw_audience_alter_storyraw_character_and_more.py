# Generated by Django 4.0.6 on 2023-09-27 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('literature', '0023_alter_ideautilization_idea_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storyraw',
            name='audience',
            field=models.TextField(blank=True, help_text="Identify the target audience for your non-fiction story (e.g., 'General readers', 'Experts').", null=True),
        ),
        migrations.AlterField(
            model_name='storyraw',
            name='character',
            field=models.TextField(blank=True, help_text="The main character in your story (e.g., 'Detective John Smith').", null=True),
        ),
        migrations.AlterField(
            model_name='storyraw',
            name='detective',
            field=models.TextField(blank=True, help_text='Introduce the detective or protagonist tasked with solving the mystery.', null=True),
        ),
        migrations.AlterField(
            model_name='storyraw',
            name='mood',
            field=models.TextField(blank=True, help_text="The mood or emotional atmosphere of your story (e.g., 'Joyful', 'Melancholic, Eerie, Tense, Gloomy, Whimsical, Nostalgic, Serene, Horrific, Humorous, Surreal, Romantic, Mysterious, Empowering, Regretful, Hopeful').", null=True),
        ),
        migrations.AlterField(
            model_name='storyraw',
            name='purpose',
            field=models.TextField(blank=True, help_text="Describe the purpose of your non-fiction story (e.g., 'Inform readers about scientific discoveries').", null=True),
        ),
        migrations.AlterField(
            model_name='storyraw',
            name='setting',
            field=models.TextField(blank=True, help_text="The primary setting of your story. An specific time, session or location (e.g., 'future, Victorian London').", null=True),
        ),
        migrations.AlterField(
            model_name='storyraw',
            name='time_period',
            field=models.TextField(blank=True, help_text='Specify the historical time period in your historical fiction story.', null=True),
        ),
        migrations.AlterField(
            model_name='storyraw',
            name='tone',
            field=models.TextField(blank=True, help_text="The tone of your story (e.g., 'Classical, Baroque, Victorian, Realistic, Modernist, Surrealistic, Naturalistic, Absurdist, Epic, Tragic, Mysterious', 'Romantic').", null=True),
        ),
        migrations.AlterField(
            model_name='storyraw',
            name='topic',
            field=models.TextField(blank=True, help_text="Specify the topic or subject of your non-fiction story (e.g., 'History of Space Exploration').", null=True),
        ),
    ]
