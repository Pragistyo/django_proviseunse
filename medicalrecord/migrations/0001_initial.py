# Generated by Django 3.1.2 on 2020-10-25 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inpatient', '0001_initial'),
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalRecords',
            fields=[
                ('medicalrecord_id', models.AutoField(primary_key=True, serialize=False)),
                ('consultdate', models.DateField()),
                ('bloodpressure', models.IntegerField()),
                ('bpmnumber', models.IntegerField()),
                ('pupil', models.CharField(max_length=100)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=4)),
                ('polyclinic', models.CharField(max_length=100)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='doctor.doctors')),
                ('inpatient_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inpatient.inpatients')),
            ],
            options={
                'db_table': 'medicalrecord',
            },
        ),
    ]
