# Generated by Django 4.0.6 on 2022-07-23 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0047_remove_interest_me_remove_languge_me'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interest',
            name='type',
        ),
    ]
