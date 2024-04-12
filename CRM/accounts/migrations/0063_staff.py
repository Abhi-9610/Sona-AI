# Generated by Django 5.0 on 2024-01-17 03:12

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0062_alter_customuser_total_rooms'),
    ]

    operations = [
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('unique_id', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('role', models.CharField(max_length=100)),
            ],
        ),
    ]