# Generated by Django 4.0.6 on 2022-07-17 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0039_alter_skillsin_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceimage',
            name='front',
            field=models.BooleanField(default=False),
        ),
    ]
