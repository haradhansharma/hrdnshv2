# Generated by Django 4.0.6 on 2022-07-12 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0002_me_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='me',
            name='me_for',
            field=models.CharField(choices=[('', 'Select You Looking For'), ('web', 'Web'), ('fashion', 'Fashion')], max_length=10, unique=True),
        ),
    ]
