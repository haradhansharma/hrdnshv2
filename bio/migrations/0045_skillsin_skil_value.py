# Generated by Django 4.0.6 on 2022-07-23 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0044_mylinks_to_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillsin',
            name='skil_value',
            field=models.IntegerField(default=0),
        ),
    ]
