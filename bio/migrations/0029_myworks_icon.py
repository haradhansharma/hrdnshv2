# Generated by Django 4.0.6 on 2022-07-14 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0028_alter_myworks_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='myworks',
            name='icon',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
