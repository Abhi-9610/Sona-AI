# Generated by Django 4.1.13 on 2023-12-01 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0057_remove_customuser_room_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='room_type',
        ),
        migrations.RemoveField(
            model_name='roomtype',
            name='room_number',
        ),
        migrations.AddField(
            model_name='customuser',
            name='room_types',
            field=models.ManyToManyField(related_name='users', to='accounts.roomtype'),
        ),
        migrations.AddField(
            model_name='roomtype',
            name='room_numbers',
            field=models.ManyToManyField(related_name='room_types', to='accounts.roomnumber'),
        ),
    ]
