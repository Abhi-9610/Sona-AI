# Generated by Django 5.0 on 2024-01-17 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0065_roomdata_owner_id_alter_staff_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomdata',
            name='owner_id',
        ),
    ]