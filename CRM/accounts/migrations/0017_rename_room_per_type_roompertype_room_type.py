# Generated by Django 4.1.13 on 2023-11-27 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_alter_roompertype_room_per_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roompertype',
            old_name='room_per_type',
            new_name='room_type',
        ),
    ]
