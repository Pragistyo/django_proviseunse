from django.db import models
from django.forms import ModelForm

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
    birthday  = models.DateField(null=True, blank=True)
    nik = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    certificate = models.CharField(max_length=100)
    datecertification = models.DateField(null=True, blank=True)
    countpatientnumber = models.IntegerField(default=0)


    class Meta:
        db_table = 'doctor'

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.firstname[0] 


class DoctorsForm(ModelForm):
    class Meta:
        model = Doctors
        fields = '__all__'
