# Generated by Django 4.2.7 on 2023-11-30 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0039_remove_customuser_staff_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(blank=True, choices=[('Manager', 'Manager'), ('House-Keeping', 'House-Keeping'), ('Laundry-Staff', 'Laundry-Staff'), ('Chef', 'Chef'), ('Room-Attendant', 'Room-Attendant'), ('Hotel-Receptionist', 'Hotel-Receptionist'), ('Res-staff', 'Restaurant-Staff')], max_length=20, null=True),
        ),
    ]
