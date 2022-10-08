# Generated by Django 4.0.6 on 2022-07-13 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0018_remove_myservice_picture_serviceimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceimage',
            name='description',
            field=models.CharField(default='', max_length=252),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='serviceimage',
            name='title',
            field=models.CharField(default='', max_length=152),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='serviceimage',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='serviceimage', to='bio.myservice'),
        ),
    ]