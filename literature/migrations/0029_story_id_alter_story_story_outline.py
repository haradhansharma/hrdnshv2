# Generated by Django 4.0.6 on 2023-09-28 02:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('literature', '0028_alter_storyraw_genre'),
    ]

    operations = [
        # migrations.AddField(
        #     model_name='story',
        #     name='id',
        #     field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        # ),
        # migrations.AlterField(
        #     model_name='story',
        #     name='story_outline',
        #     field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='literature.storyoutline'),
        # ),
    ]
