# Generated by Django 4.1.13 on 2023-11-28 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_remove_customuser_rooms_per_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='room_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
