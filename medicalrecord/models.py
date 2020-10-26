from django.db import models
from inpatient.models import Inpatients
from doctor.models import Doctors
from django.forms import ModelForm

# Create your models here.
class MedicalRecords(models.Model):
    medicalrecord_id = models.AutoField(primary_key=True, serialize=True)
    inpatient_id = models.ForeignKey(Inpatients, on_delete=models.DO_NOTHING, db_column= "inpatient_id")
    doctor_id = models.ForeignKey(Doctors, on_delete=models.DO_NOTHING, db_column= "doctor_id")
    consultdate = models.DateField()
    bloodpressure = models.IntegerField()
    bpmnumber = models.IntegerField()
    pupil = models.CharField(max_length=100)
    temperature = models.DecimalField(max_digits=4, decimal_places=2)
    polyclinic = models.CharField(max_length=100)

    class Meta :
        db_table = 'medicalrecord'

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.medicalrecord_id


class MedicalRecordsForm(ModelForm):
    class Meta:
        model = MedicalRecords
        fields = '__all__'

