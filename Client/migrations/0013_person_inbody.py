# Generated by Django 4.0.3 on 2022-04-15 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0012_remove_person_inbody'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='Inbody',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
