# Generated by Django 5.0 on 2024-01-17 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0067_roomdata_owner_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomdata',
            name='total_rooms',
        ),
    ]
