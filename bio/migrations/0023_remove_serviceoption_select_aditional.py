# Generated by Django 4.0.6 on 2022-07-13 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0022_serviceoption_select_aditional'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceoption',
            name='select_aditional',
        ),
    ]
