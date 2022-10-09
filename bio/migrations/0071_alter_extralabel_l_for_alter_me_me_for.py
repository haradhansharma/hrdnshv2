# Generated by Django 4.0.6 on 2022-10-09 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0070_alter_extralabel_l_for_alter_me_me_for_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extralabel',
            name='l_for',
            field=models.CharField(choices=[('', 'Choose the area ...'), ('web', 'Web Development'), ('fashion', 'Fashion Technology')], default='web', max_length=10),
        ),
        migrations.AlterField(
            model_name='me',
            name='me_for',
            field=models.CharField(choices=[('', 'Choose the area ...'), ('web', 'Web Development'), ('fashion', 'Fashion Technology')], max_length=10, unique=True),
        ),
    ]