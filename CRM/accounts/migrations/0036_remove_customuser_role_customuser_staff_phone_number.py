# Generated by Django 4.2.7 on 2023-11-29 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0035_delete_customtoken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='role',
        ),
        migrations.AddField(
            model_name='customuser',
            name='staff_phone_number',
            field=models.CharField(default=None, max_length=13, null=True, unique=True),
        ),
    ]
