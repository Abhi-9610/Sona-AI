from django.db import models
import uuid
# Create your models here.

class Resturant(models.Model):
    name=models.CharField(max_length=40)
    price=models.IntegerField()
    
    desc=models.CharField(max_length=100)
    quantity=models.CharField(max_length=10)
    item_id=models.UUIDField(default=uuid.uuid4,unique=True)
    category=models.CharField(max_length=100)
    restro_id=models.UUIDField(default=uuid.uuid4,unique=True)
    restro_owner_id=models.CharField(max_length=100)
    image=models.ImageField(upload_to='public/restro')


class bar(models.Model):
    name=models.CharField(max_length=40)
    price=models.IntegerField()
    desc=models.CharField(max_length=100)
    quantity=models.CharField(max_length=10)
    item_id=models.UUIDField(default=uuid.uuid4,unique=True)
    bar_id=models.UUIDField(default=uuid.uuid4,unique=True)
    image=models.ImageField(upload_to='public/bar/')
    bar_owner_id=models.CharField(max_length=100)

class inverntory(models.Model):
    name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='public/inventory/')
    quantity=models.CharField(max_length=120)
    price=models.CharField(max_length=1000000)
    status=models.CharField(max_length=10)
    unique_id=models.UUIDField(default=uuid.uuid4,unique=True)
    owner_id=models.CharField(max_length=120)
    item_for=models.CharField(max_length=1000)
    


class laundry(models.Model):
    name=models.CharField(max_length=40)
    price=models.IntegerField()
    desc=models.CharField(max_length=100)
    unique_id=models.UUIDField(default=uuid.uuid4,unique=True)
    image=models.ImageField(upload_to='public/laundry/')
    owner_id=models.CharField(max_length=100)