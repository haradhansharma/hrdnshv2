# Generated by Django 4.0.6 on 2022-07-14 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0027_myworks_workimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myworks',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
