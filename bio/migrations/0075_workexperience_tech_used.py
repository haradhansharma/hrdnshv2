# Generated by Django 4.0.6 on 2023-03-14 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0074_myservice_created_myservice_updated_myworks_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workexperience',
            name='tech_used',
            field=models.ManyToManyField(related_name='skillsinex', to='bio.myskills'),
        ),
    ]
