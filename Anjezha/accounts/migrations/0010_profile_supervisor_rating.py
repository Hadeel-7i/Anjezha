# Generated by Django 4.2.7 on 2023-12-30 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_profile_department_delete_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='supervisor_rating',
            field=models.IntegerField(default=0),
        ),
    ]