# Generated by Django 4.1.13 on 2023-11-30 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0043_customuser_room_number_customuser_room_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='services',
            field=models.CharField(blank=True, choices=[('RES', 'Restaurant'), ('SP', 'Swimming-Pool'), ('Bar', 'Bar'), ('Laundry', 'Laundry'), ('Parking', 'Parking')], max_length=10, null=True),
        ),
    ]
