# Generated by Django 4.0.6 on 2023-03-14 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0077_remove_workexperience_tech_used'),
    ]

    operations = [
        migrations.AddField(
            model_name='workexperience',
            name='techn_used',
            field=models.ManyToManyField(related_name='skillsinex', to='bio.skillsin'),
        ),
    ]
