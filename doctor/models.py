from datetime import datetime
from django.db import models

# Create your models here.
class Doctors (models.Model):
    doctor_id = models.AutoField(primary_key=True, serialize=True)
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    mobilenumber = models.CharField(max_length=25)
    gender = models.CharField(max_length=25)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    birthplace = models.CharField(max_length=100)
    birthday  = models.DateTimeField(null=True)
    nik = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    certificate = models.CharField(max_length=100)
    datecertification = models.DateTimeField(null=True)
    countpatientnumber = models.IntegerField(default=0)


    class Meta:
        db_table = 'doctor'

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.firstname +  ' ' +  self.middlename + ' ' + self.lastname + ' , NIK: '+ self.nik+ '; '
