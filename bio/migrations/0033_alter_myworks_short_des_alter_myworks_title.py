# Generated by Django 4.0.6 on 2022-07-14 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0032_alter_myworks_icon_alter_myworks_short_des_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myworks',
            name='short_des',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='myworks',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
