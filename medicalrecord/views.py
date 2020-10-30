# from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import MedicalRecords
from .models import MedicalRecordsForm
from . import transformer
from . import rawQuery
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
        # nanti coba ganti pake transaction
        queryInsert = rawQuery.queryInsert
        valueInsert = [
            json_data['inpatient_id'],json_data['doctor_id'], json_data['consultdate'], json_data['bloodpressure'],json_data['bpmnumber'],
            json_data['pupil'],json_data['temperature'],json_data['polyclinic']
        ]
        print('================== create medical record ====================== ')
        with connection.cursor() as cursor:
            cursor.execute(queryInsert, valueInsert)
            latest_obj = cursor.fetchall()[0] #<class 'tuple>
            # latest_obj =  (
            # '(15,1,5,2019-03-19,105,90,normal,36.80,GI)', 10, 'Ridho', 'Ardhi', 'Syaiful'
            # )
            arrDataInserted = latest_obj[0][1:-1].split(',') #[15,1,5,2019-03-19,105,90,normal,36.80,GI]
            doctorName = latest_obj[2]+ ' ' +latest_obj[3]+'  ' + latest_obj[4]
            doctorInfo = {"doctorName": doctorName, "currentCountpatientnumber": latest_obj[1]}

            dictResult= transformer.dictTransformCreate(arrDataInserted, doctorInfo)
            print("==============RESULT=================")
            print(type(dictResult))
            result = json.dumps(dictResult)
        return HttpResponse(result, content_type='application/json')

@csrf_exempt
def show(request, medicalrecord_id):
    if request.method =='GET':
        print('GET')
        med_rec_one = MedicalRecords.objects.get(pk=medicalrecord_id)
        data = serializers.serialize("json", [med_rec_one, ])
        return HttpResponse(data)

    elif request.method =='DELETE':
        # del_med_rec = MedicalRecords.objects.get(pk=medicalrecord_id).delete()
        queryRemove =  rawQuery.queryRemove
        valueRemove = [medicalrecord_id, medicalrecord_id]
        with connection.cursor() as cursor:
            cursor.execute(queryRemove, valueRemove)
            row = cursor.fetchall()[0]
            print('================= DELETE ROW ====================')
            print(type(row))
            print(row)
            #row = (20, 1, 5, datetime.date(2019, 3, 19), 105, 90, 'normal', Decimal('36.80'), 'GI')
            deleteInfo = transformer.dictTransformMedicalRecord(row)
            result = json.dumps(deleteInfo)
        return HttpResponse(result, content_type='application/json')

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
        print('============ json =================')
        print(type( request.body))
        print( request.body)
        json_data = json.loads( request.body)
        print(json_data)

        queryGetByDate=''
        valueGetByDate = []

        if json_data['polyclinic'] == None or json_data['polyclinic'] == '' :
            print("-----------------NO POLYCLINIC-------------------")
            valueGetByDate.extend([json_data['dateFrom'], json_data['dateTo']])
            queryGetByDate = rawQuery.queryMedicalRecordDateRange
            
        elif json_data['polyclinic'] :
            print("+++++++++++ WITH POLYCLINIC +++++++++++")
            valueGetByDate.extend([json_data['polyclinic'], json_data['dateFrom'], json_data['dateTo']])
            queryGetByDate = rawQuery.queryMedicalRecordDateRangePolyclinic

        with connection.cursor() as cursor:
            cursor.execute(queryGetByDate, valueGetByDate)
            row = cursor.fetchall()
            print("=================== RESULT ROW =====================")
            print(type(row))
            print(row)

            arrPolyclinic = []

            for val in row:
                arrPolyclinic.append( val[0] )

            rowInfo = [arrPolyclinic, row[0][1], row[0][2], row[0][3], row[0][4], row[0][5] ]
            # ('Polyclinic', consult_total, O, A, B, AB)
            # [ 
            # ('GI', 9, 9, 0, 0, 0), ('GI', 9, 9, 0, 0, 0), ('GI', 9, 9, 0, 0, 0), 
            # ('GI', 9, 9, 0, 0, 0), ('GI', 9, 9, 0, 0, 0), ('GI', 9, 9, 0, 0, 0), 
            # ('GI', 9, 9, 0, 0, 0), ('GI', 9, 9, 0, 0, 0), ('GI', 9, 9, 0, 0, 0)
            # ]
            dictResult = transformer.dictTransformGetByDate(rowInfo)
            result = json.dumps(dictResult)
        # return HttpResponse('getBydatePolyclinic:')
        return HttpResponse(result, content_type='application/json')

