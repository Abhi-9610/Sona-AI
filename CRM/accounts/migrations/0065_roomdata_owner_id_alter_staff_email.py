# Generated by Django 5.0 on 2024-01-17 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0064_customuser_unique_id_staff_owner_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomdata',
            name='owner_id',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='staff',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
