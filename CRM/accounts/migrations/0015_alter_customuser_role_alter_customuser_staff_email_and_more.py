# Generated by Django 4.1.13 on 2023-11-27 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_customuser_role_alter_customuser_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('Manager', 'Manager'), ('House-Keeping', 'House-Keeping'), ('Laundry-Staff', 'Laundry-Staff'), ('Chef', 'Chef'), ('Room-Attendant', 'Room-Attendant'), ('Hotel-Receptionist', 'Hotel-Receptionist')], default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='staff_email',
            field=models.EmailField(default=None, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='staff_name',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
