# Generated by Django 4.0.6 on 2023-09-23 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('literature', '0004_remove_storyraw_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storyraw',
            name='genre',
            field=models.CharField(choices=[('Fiction', 'Fiction'), ('Non-Fiction', 'Non-Fiction'), ('Poetry', 'Poetry'), ('Fantasy', 'Fantasy'), ('Mystery', 'Mystery'), ('Historical Fiction', 'Historical Fiction'), ('Science Fiction', 'Science Fiction'), ('Romance', 'Romance'), ('Horror', 'Horror'), ('Memoir', 'Memoir'), ('Satire', 'Satire'), ('Fable', 'Fable'), ("Children's Literature", "Children's Literature")], help_text='Select the genre of your story.', max_length=50),
        ),
        migrations.AlterField(
            model_name='storyraw',
            name='mood',
            field=models.CharField(blank=True, help_text="The mood or emotional atmosphere of your story (e.g., 'Joyful', 'Melancholic, Eerie, Tense, Gloomy, Whimsical, Nostalgic, Serene, Horrific, Humorous, Surreal, Romantic, Mysterious, Empowering, Regretful, Hopeful').", max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='storyraw',
            name='rhyme_meter',
            field=models.CharField(blank=True, help_text="Specify the rhyme scheme or meter for your poem (e.g., 'ABAB', 'Haiku, Sonnet, Limerick, Villanelle, Pantoum, Sestina, Tanka, Ghazal, Ode, Ballad, Triolet').", max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='storyraw',
            name='setting',
            field=models.CharField(blank=True, help_text="The primary setting of your story. An specific time, session or location (e.g., 'future, Victorian London').", max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='storyraw',
            name='style',
            field=models.CharField(blank=True, help_text="The narrative style (e.g., 'First-person', 'Third-person, Third-Person Limited, Third-Person Omniscient, Second-Person, Epistolary, Stream of Consciousness, Multi-Person, Unreliable Narrator, Framed Narrative').", max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='storyraw',
            name='theme',
            field=models.CharField(blank=True, help_text="The central theme of your story (e.g., 'Love', 'Adventure, Conflict, Identity, Coming of Age, Power and Corruption, Justice and Injustice, Isolation and Alienation, Nature vs. Nurture, Freedom and Oppression, Death and Mortality, Friendship, Ambition and Desire, Society and Social Change, Betrayal, Memory and Nostalgia, Hope and Despair, Technology and Progress, Family, Survival, Fate and Free Will, Redemption').", max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='storyraw',
            name='tone',
            field=models.CharField(blank=True, help_text="The tone of your story (e.g., 'Classical, Baroque, Victorian, Realistic, Modernist, Surrealistic, Naturalistic, Absurdist, Epic, Tragic, Mysterious', 'Romantic').", max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='storyraw',
            name='type',
            field=models.CharField(default='', help_text="The type of your literature (e.g., 'Essay, Drama, Poem, Story, Novel, Short Story, Epic').", max_length=200),
            preserve_default=False,
        ),
    ]
