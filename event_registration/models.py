from django.db import models
from django.contrib.auth.models import User

class Participant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to Django's User model
    register_number = models.CharField(max_length=20, unique=True)
    college_name = models.CharField(max_length=255)
    department = models.CharField(max_length=100)
    whatsapp_number = models.CharField(max_length=15)
    
    YEAR_CHOICES = [
        ('1', '1st Year'),
        ('2', '2nd Year'),
        ('3', '3rd Year'),
        ('4', '4th Year'),
    ]
    year_of_study = models.CharField(max_length=1, choices=YEAR_CHOICES)
    coupon_purchased = models.BooleanField(default=False)
    attendance = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.register_number}"


class event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    date = models.DateField()
    time = models.TimeField(null=True,blank=True)
    rules_and_regulations = models.TextField(null=True,blank=True)
    venue = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to='event_registration/images',null=True,blank=True)
    participants = models.ManyToManyField(Participant,related_name='events',blank=True)
    team_size = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.name
    
class organizer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    event = models.ForeignKey(event,on_delete=models.CASCADE,related_name='organizers')

    def __str__(self):
        return self.name
    
class teammate(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    event = models.ForeignKey(event,on_delete=models.CASCADE,related_name='teammates')
    team_of = models.ForeignKey(Participant,on_delete=models.CASCADE,related_name='teammates')

    def __str__(self):
        return self.name