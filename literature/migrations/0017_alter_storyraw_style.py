# Generated by Django 4.0.6 on 2023-09-25 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('literature', '0016_alter_ideautilization_idea_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storyraw',
            name='style',
            field=models.TextField(blank=True, help_text="The narrative style (e.g., 'First-person', 'Third-person, Third-Person Limited, Third-Person Omniscient, Second-Person, Epistolary, Stream of Consciousness, Multi-Person, Unreliable Narrator, Framed Narrative').", max_length=50, null=True),
        ),
    ]
