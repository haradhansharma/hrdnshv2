# Generated by Django 4.0.6 on 2022-07-14 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0031_alter_myworks_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myworks',
            name='icon',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='myworks',
            name='short_des',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='myworks',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
