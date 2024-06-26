# Generated by Django 4.1.13 on 2023-11-30 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0042_roomtype_remove_customuser_room_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='room_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='room_type',
            field=models.CharField(choices=[('DEL', 'Delux'), ('SND', 'Standard'), ('AC', 'AC'), ('Non-AC', 'Non-AC'), ('Semi_delux', 'Semi-Delux')], max_length=10, null=True),
        ),
    ]
