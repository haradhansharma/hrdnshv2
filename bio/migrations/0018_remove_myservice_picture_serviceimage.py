# Generated by Django 4.0.6 on 2022-07-13 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0017_alter_serviceoption_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myservice',
            name='picture',
        ),
        migrations.CreateModel(
            name='ServiceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='service_image')),
                ('alt', models.CharField(max_length=152)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myserviceimage', to='bio.myservice')),
            ],
        ),
    ]
