# Generated by Django 4.0.6 on 2023-09-24 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('literature', '0011_storyraw_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storyraw',
            name='title',
            field=models.CharField(blank=True, help_text='It an keep blank to add from response of chatGPT', max_length=250, null=True),
        ),
    ]
