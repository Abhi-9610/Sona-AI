# Generated by Django 4.1.13 on 2023-12-01 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0054_remove_roomnumber_room_type_alter_roomtype_room_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomtype',
            name='room_number',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='room_data', to='accounts.roomnumber'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='room_type',
            field=models.CharField(max_length=50),
        ),
    ]