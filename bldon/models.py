import datetime
from django.db import models
from django.utils import timezone

class BloodGroup(models.Model):
    name = models.CharField(max_length=5)
    def __str__(self):
        return self.name

class Donor(models.Model):

    class Meta:
        managed = True
        app_label = 'bldon'
    name = models.CharField(max_length= 100 , unique=True)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length= 50)
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    gender = models.CharField(max_length=10)
    last_donate = models.DateField( default = datetime.date.today() - datetime.timedelta(days = 100))
    password = models.CharField(max_length = 100, default = '123')
    reward = models.IntegerField(default = 0)

    def __str__(self):
        return self.name

    def retpass(self):
        return self.password
