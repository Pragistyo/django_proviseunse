from django.shortcuts import render
from django.http import HttpResponse
from .models import Inpatients
from .models import InpatientsForm
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import psycopg2
from django.http import JsonResponse


import json

# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'GET':
        data = serializers.serialize("json", Inpatients.objects.all())
        return HttpResponse(data)

    elif request.method == 'POST':
        json_data = json.loads(request.body)
        formInpatients = InpatientsForm(json_data)
        if formInpatients.is_valid():
            print('inpatient create valid')
            formInpatients.save()
        return HttpResponse('create inpatient data succeed')
        

@csrf_exempt
def show(request, inpatient_id):
    if request.method == 'GET':
        try:
            result = Inpatients.objects.get(pk=inpatient_id)
            data =serializers.serialize("json", [result,])
            return HttpResponse(data)
        except ObjectDoesNotExist:
            print(ObjectDoesNotExist)
            return JsonResponse({"status":404,"message":'inpatient_id does not exist'})
            # return HttpResponse('inpatient_id does not exist')

    elif request.method == 'DELETE':
        try:
            result = Inpatients.objects.get(pk=inpatient_id).delete()
            return HttpResponse('Succeed delete record', result)
        except ObjectDoesNotExist as e:
            return JsonResponse({"status":404,"message":'inpatient_id does not exist'})

    elif request.method == 'PUT':
        try:
            json_data = json.loads(request.body)
            result = Inpatients.objects.filter(pk=inpatient_id).update(
                firstname = json_data['firstname'], 
                middlename = json_data['middlename'], 
                lastname = json_data['lastname'], 
                mobilenumber = json_data['mobilenumber'], 
                gender = json_data['gender'], 
                address1 = json_data['address1'], 
                address2 = json_data['address2'], 
                state = json_data['state'], 
                city = json_data['city'], 
                zipcode = json_data['zipcode'], 
                birthplace = json_data['birthplace'], 
                birthday  = json_data['birthday'],  
                bloodtype = json_data['bloodtype'], 
            )
            if result == 0:
                return HttpResponse('Inpatient not found')
            elif result == 1:
                return HttpResponse('Successfully update Inpatient record')
        except ObjectDoesNotExist as e:
            return JsonResponse({"status":404,"message":'inpatient_id does not exist'})
        
            
