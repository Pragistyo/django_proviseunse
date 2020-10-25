from django.db import models
from django.forms import ModelForm


# Create your models here.
class Inpatients (models.Model):
    inpatient_id = models.AutoField(primary_key=True, serialize=True)
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
    bloodtype = models.CharField(max_length=2)

    class Meta:
        db_table = 'inpatient'
        
    def __str__(self):
        return self.firstname[0] 

class InpatientsForm(ModelForm):
    class Meta:
        model = Inpatients
        fields = '__all__'
