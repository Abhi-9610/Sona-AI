# Generated by Django 4.2.7 on 2023-11-29 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0038_tokenblacklist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='staff_phone_number',
        ),
    ]