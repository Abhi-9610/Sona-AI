# Generated by Django 4.1.13 on 2023-11-26 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_roomtype_room'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roomtype',
            old_name='name',
            new_name='services',
        ),
    ]