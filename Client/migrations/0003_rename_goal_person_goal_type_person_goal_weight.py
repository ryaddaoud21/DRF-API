# Generated by Django 4.0.3 on 2022-03-26 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0002_person_train_alter_person_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='Goal',
            new_name='Goal_Type',
        ),
        migrations.AddField(
            model_name='person',
            name='Goal_Weight',
            field=models.CharField(choices=[('1 ', '1/4 Kgs'), ('2', '1/2 Kgs'), ('3', '1 Kgs')], default='1', max_length=10),
        ),
    ]
