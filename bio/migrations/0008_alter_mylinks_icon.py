# Generated by Django 4.0.6 on 2022-07-12 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0007_alter_mylinks_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mylinks',
            name='icon',
            field=models.TextField(),
        ),
    ]
