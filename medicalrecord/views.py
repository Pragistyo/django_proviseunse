# from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import MedicalRecords
from .models import MedicalRecordsForm
from django.views.decorators.csrf import csrf_exempt
from django.db import connection, transaction

import json
# Create your views here.

@csrf_exempt
def index(request):
    if request.method =='GET':
        med_rec = MedicalRecords.objects.all()
        result = serializers.serialize("json", med_rec)
        return HttpResponse(result)
    elif request.method == 'POST':
        json_data = json.loads(request.body)
        print(json_data)
        formMedicalRecord = MedicalRecordsForm(json_data)
        if formMedicalRecord.is_valid():
            formMedicalRecord.save()
            return HttpResponse('data added')
        return HttpResponse('form_data not valid')

@csrf_exempt
def show(request, medicalrecord_id):
    if request.method =='GET':
        print('GET')
        med_rec_one = MedicalRecords.objects.get(pk=medicalrecord_id)
        data = serializers.serialize("json", [med_rec_one, ])
        return HttpResponse(data)
    elif request.method =='DELETE':
        # del_med_rec = MedicalRecords.objects.get(pk=medicalrecord_id).delete()
        queryRemove =  '''
        WITH u AS (
            UPDATE doctor 
            SET countpatientnumber = countpatientnumber - 1
            WHERE 
                doctor.doctor_id = (SELECT doctor_id FROM medicalrecord WHERE medicalrecord_id = %s) 
            RETURNING *
        )
        DELETE from medicalrecord WHERE medicalrecord_id = %s
        RETURNING *
        '''
        valueRemove = [medicalrecord_id, medicalrecord_id]
        with connection.cursor() as cursor:
            row = cursor.execute(queryRemove, valueRemove)
            print('row')
            print(row)
        return HttpResponse('data deleted')
    elif request.method == 'PUT':
        json_data = json.loads(request.body)
        update_med_rec = MedicalRecords.objects.filter(pk=medicalrecord_id).update(
            inpatient_id = json_data['inpatient_id'],  
            doctor_id = json_data['doctor_id'], 
            consultdate = json_data['consultdate'], 
            bloodpressure = json_data['bloodpressure'], 
            bpmnumber = json_data['bpmnumber'], 
            pupil = json_data['pupil'],
            temperature = json_data['temperature'], 
            polyclinic = json_data['polyclinic']
        )
        if update_med_rec == 1:
            return HttpResponse('data medical record updated successfully')
        elif update_med_rec == 0:
            return HttpResponse('RECORD NOT FOUND')

@csrf_exempt
def customQuery(request):
    if request.method =='POST':
        json_data = json.loads(request.body)
        # nanti coba ganti pake transaction
        queryInsert = '''
        WITH i AS (
            INSERT INTO medicalrecord
            (medicalrecord_id, inpatient_id, doctor_id, consultdate, bloodpressure, bpmnumber ,pupil, temperature, polyclinic)
            VALUES 
            (DEFAULT, %s,%s,%s, %s,
            %s, %s, %s,%s)
            RETURNING *
        )
        UPDATE doctor AS a
            SET countpatientnumber = countpatientnumber + 1
            FROM i
            WHERE i.doctor_id = a.doctor_id
        RETURNING i, countpatientnumber, firstname, middlename, lastname
        '''
        valueInsert = [
            json_data['inpatient_id'],json_data['doctor_id'], json_data['consultdate'], json_data['bloodpressure'],json_data['bpmnumber'],
            json_data['pupil'],json_data['temperature'],json_data['polyclinic']
        ]
        print('======================================== sampe sini masuk')
        with connection.cursor() as cursor:
            cursor.execute(queryInsert, valueInsert)
            latest_obj = MedicalRecords.objects.latest('medicalrecord_id')
            print('latest_obj')
            print(type(latest_obj))
            # print(latest_obj)
            result = serializers.serialize("json", latest_obj)
        return HttpResponse(result)

