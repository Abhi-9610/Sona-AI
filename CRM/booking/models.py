from django.db import models
import uuid

class Bookingdetails(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Transgender', 'Transgender'),
        ('LGBTQ', 'LGBTQ'),
    ]

    NATIONALITY_CHOICES = [
        ('indian', 'INDIAN'),
        ('non-indian', 'NON_INDIAN'),
    ]
    GOVT_ID=[
        ('Aadhar card','Aadhar Card'),
        ('Passport','PassPort'),
        ('DL','Driving License'),
        ('VOter-Id','Voter-id'),
        ('Pan-card','Pan Card')
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.IntegerField()
    no_guest = models.IntegerField()
    no_room = models.IntegerField()
    date_from = models.DateField()
    date_to = models.DateField()
    # room_number = models.CharField(max_length=250)
    booking_id = models.UUIDField(default=uuid.uuid4)
    hotel_id = models.CharField(max_length=1000)
    govt_id = models.CharField(max_length=100,choices=GOVT_ID)
    govt_id_no = models.IntegerField()
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    nationality = models.CharField(max_length=15, choices=NATIONALITY_CHOICES)
    no_adult=models.IntegerField()
    no_children=models.IntegerField()