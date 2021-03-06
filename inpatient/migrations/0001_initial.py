# Generated by Django 3.1.2 on 2020-10-25 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inpatients',
            fields=[
                ('inpatient_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=100)),
                ('middlename', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('mobilenumber', models.CharField(max_length=25)),
                ('gender', models.CharField(max_length=25)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=100)),
                ('birthplace', models.CharField(max_length=100)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('bloodtype', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'inpatient',
            },
        ),
    ]
