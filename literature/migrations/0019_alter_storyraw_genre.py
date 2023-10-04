# Generated by Django 4.0.6 on 2023-09-25 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('literature', '0018_alter_storyraw_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storyraw',
            name='genre',
            field=models.CharField(choices=[('Fiction', 'Fiction'), ('Non-Fiction', 'Non-Fiction'), ('Poetry', 'Poetry'), ('Fantasy', 'Fantasy'), ('Mystery', 'Mystery'), ('Historical Fiction', 'Historical Fiction'), ('Science Fiction', 'Science Fiction'), ('Romance', 'Romance'), ('Horror', 'Horror'), ('Memoir', 'Memoir'), ('Satire', 'Satire'), ('Fable', 'Fable'), ('Social Realism', 'Social Realism'), ('Children Literature', 'Children Literature')], help_text='Select the genre of your story.', max_length=50),
        ),
    ]
