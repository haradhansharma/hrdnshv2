# Generated by Django 4.0.6 on 2023-09-24 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('literature', '0008_delete_story'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('story_outline', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='literature.storyoutline')),
                ('sigment_story', models.TextField()),
            ],
        ),
    ]