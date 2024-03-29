# Generated by Django 4.0.6 on 2023-09-27 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('literature', '0024_alter_storyraw_audience_alter_storyraw_character_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storyraw',
            name='genre',
            field=models.CharField(blank=True, choices=[('Fiction', 'Fiction'), ('Non-Fiction', 'Non-Fiction'), ('Poetry', 'Poetry'), ('Fantasy', 'Fantasy'), ('Mystery', 'Mystery'), ('Historical Fiction', 'Historical Fiction'), ('Science Fiction', 'Science Fiction'), ('Romance', 'Romance'), ('Horror', 'Horror'), ('Memoir', 'Memoir'), ('Satire', 'Satire'), ('Fable', 'Fable'), ('Social Realism', 'Social Realism'), ('Children Literature', 'Children Literature')], help_text='Select the genre of your story.', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='storyraw',
            name='type',
            field=models.CharField(blank=True, help_text="The type of your literature (e.g., 'Essay, Drama, Poem, Story, Novel, Short Story, Epic').", max_length=200, null=True),
        ),
    ]
