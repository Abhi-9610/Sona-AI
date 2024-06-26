# Generated by Django 4.1.13 on 2023-12-05 07:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0059_remove_roomtype_room_numbers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='total_rooms',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.CreateModel(
            name='Roomdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_types', models.CharField(max_length=20)),
                ('room_number', models.CharField(blank=True, default=None, max_length=1000)),
                ('total_rooms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
