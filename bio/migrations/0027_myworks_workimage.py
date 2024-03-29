# Generated by Django 4.0.6 on 2022-07-14 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0026_myservice_dark_class_myservice_light_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyWorks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=252)),
                ('slug', models.SlugField()),
                ('short_des', models.TextField(max_length=252)),
                ('Description', models.TextField()),
                ('category', models.ManyToManyField(related_name='workcategories', to='bio.servicecategory')),
                ('me', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myworks', to='bio.me')),
                ('skills_involved', models.ManyToManyField(related_name='worksinservice', to='bio.skillsin')),
            ],
        ),
        migrations.CreateModel(
            name='WorkImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='work_image')),
                ('title', models.CharField(max_length=152)),
                ('description', models.CharField(max_length=252)),
                ('alt', models.CharField(max_length=152)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workimage', to='bio.myworks')),
            ],
        ),
    ]
