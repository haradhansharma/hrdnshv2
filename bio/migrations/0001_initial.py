# Generated by Django 4.0.6 on 2022-07-12 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('me_for', models.CharField(choices=[('', 'Select You Looking For'), ('web', 'Web'), ('fashion', 'Fashion')], max_length=10)),
                ('title', models.CharField(max_length=252)),
                ('summary', models.TextField()),
            ],
        ),
    ]
