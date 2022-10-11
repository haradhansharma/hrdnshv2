# Generated by Django 4.0.6 on 2022-10-11 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0073_myservice_dark_link_class_myservice_light_link_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='myservice',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='myservice',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='myworks',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='myworks',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='servicecategory',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='servicecategory',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
