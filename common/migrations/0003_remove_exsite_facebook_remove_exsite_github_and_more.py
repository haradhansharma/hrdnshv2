# Generated by Django 4.0.6 on 2022-10-09 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_remove_exsite_facebook_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exsite',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='exsite',
            name='github',
        ),
        migrations.RemoveField(
            model_name='exsite',
            name='linkedin',
        ),
        migrations.RemoveField(
            model_name='exsite',
            name='twitter',
        ),
    ]
