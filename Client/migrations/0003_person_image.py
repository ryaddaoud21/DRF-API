# Generated by Django 4.0.3 on 2022-03-21 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0002_alter_person_height_alter_person_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='Image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
