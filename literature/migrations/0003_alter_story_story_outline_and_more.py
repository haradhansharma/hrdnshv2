# Generated by Django 4.0.6 on 2023-09-23 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('literature', '0002_storyraw_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='story_outline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outline_base_story', to='literature.storyoutline'),
        ),
        migrations.AlterField(
            model_name='storyoutline',
            name='story_raw',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storyoutline', to='literature.storyraw'),
        ),
    ]
