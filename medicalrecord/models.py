from django.db import models
from inpatient.models import Inpatients
from doctor.models import Doctors

# Create your models here.
class MedicalRecords(models.Model):
    medicalrecord_id = models.AutoField(primary_key=True, serialize=True)
    inpatient_id = models.ForeignKey(Inpatients, on_delete=models.DO_NOTHING)
    doctor_id = models.ForeignKey(Doctors, on_delete=models.DO_NOTHING)
    consultdate = models.DateTimeField()
    bloodpressure = models.IntegerField()
    bpmnumber = models.IntegerField()
    pupil = models.CharField(max_length=100)
    temperature = models.DecimalField(max_digits=4, decimal_places=2)
    polyclinic = models.CharField(max_length=100)

    class Meta :
        db_table = 'medicalrecord'
