# Generated by Django 4.0.6 on 2022-07-23 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0046_languge_interest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interest',
            name='me',
        ),
        migrations.RemoveField(
            model_name='languge',
            name='me',
        ),
    ]
