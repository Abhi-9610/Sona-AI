# Generated by Django 4.2.7 on 2023-11-29 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0034_customtoken'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomToken',
        ),
    ]