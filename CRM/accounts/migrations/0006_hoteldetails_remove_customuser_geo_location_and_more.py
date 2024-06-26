# Generated by Django 4.1.13 on 2023-11-26 06:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_name_roomtype_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_hotel', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True, unique=True)),
                ('hotel_name', models.CharField(blank=True, max_length=25, null=True)),
                ('reg_num', models.CharField(blank=True, max_length=20, null=True)),
                ('gst_number', models.CharField(blank=True, max_length=15, null=True)),
                ('official_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('hotel_logo', models.ImageField(blank=True, null=True, upload_to='hotel_logos/')),
                ('geo_location', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='geo_location',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='gst_number',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='hotel_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='id_hotel',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='official_email',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='reg_num',
        ),
        migrations.AddField(
            model_name='customuser',
            name='hotel_details',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.hoteldetails'),
        ),
    ]
