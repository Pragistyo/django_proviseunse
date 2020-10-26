# from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import MedicalRecords
from .models import MedicalRecordsForm
from django.views.decorators.csrf import csrf_exempt

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
        del_med_rec = MedicalRecords.objects.get(pk=medicalrecord_id).delete()
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


