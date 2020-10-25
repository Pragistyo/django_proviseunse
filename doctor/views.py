from django.shortcuts import render
from django.http import HttpResponse
from .models import Doctors
from .models import DoctorsForm
from django.core import serializers

from . import transformer
from django_api.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.db import  connection

import json
import datetime
# import objc

# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'GET':
        # data = serializers.serialize("json", Doctors.objects.all())
        doctors = Doctors.objects.all()
        doctors = transformer.transform(doctors)
        return Response.ok(values = doctors)
        # return HttpResponse(doctors)
    elif request.method == 'POST':
        json_data = json.loads(request.body)
        birthday_str = json_data['birthday']
        year,month,day = birthday_str.split('-') 
        bdayObj = datetime.date(int(year),int(month),int(day))
        print('==================')
        print(type(year), month, day)#string
        print('==================')
        print (bdayObj)
        print(type(bdayObj))#<class 'datetime.date>
      
        # birthday_time_obj = datetime.datetime.strptime(birthday_str, '%Y-%m-%d')



        # doctor = Doctors()
        # doctor.firstname= json_data['firstname']
        # doctor.middlename= json_data['middlename']
        # doctor.lastname= json_data['lastname']
        # doctor.mobilenumber= json_data['mobilenumber']
        # doctor.gender= json_data['gender']
        # doctor.address1= json_data['address1']
        # doctor.address2= json_data['address2']
        # doctor.state= json_data['state']
        # doctor.city= json_data['city']
        # doctor.zipcode= json_data['zipcode']
        # doctor.birthplace= json_data['birthplace']
        # doctor.birthday = json_data['birthday']
        # doctor.nik= json_data['nik']
        # doctor.specialization= json_data['specialization']
        # doctor.certificate= json_data['certificate']
        # doctor.datecertification= json_data['datecertification']
        # doctor.countpatientnumber= json_data['countpatientnumber']
        # doctorObj = transformer.transformJsonToObject(json_data)
        # print(type(doctor.firstname))
        # print (doctor.firstname, type(doctor.lastname), doctor.birthday)
        # print(doctor)
        # doctor.save()

        # return Response.ok(
        #     values= transformer.singleTransform(doctor),
        #     message="recorded"
        # )

        formDoctor = DoctorsForm(json_data)
        print (formDoctor.is_valid())
        if formDoctor.is_valid():
            print('valid')
            formDoctor.save()
        return HttpResponse('data added')
@csrf_exempt
def show (request, doctor_id):
    val = doctor_id
    if request.method == 'GET':
        query = 'SELECT * FROM doctor WHERE doctor_id = %s'
        doctorRaw = Doctors.objects.raw(query, [val])
        print(doctorRaw)
        if doctorRaw.__len__() == 0:
            return HttpResponse('Doctor not found')
        result = serializers.serialize('json', doctorRaw)
        return HttpResponse(result)
    elif request.method == 'DELETE':
        query = 'DELETE FROM doctor WHERE doctor_id = %s'
        result =  Doctors.objects.raw(query,[val])
        return HttpResponse('doctor with doctor_id = %s, deleted' % val)
    elif request.method == 'PUT':
        json_data = json.loads(request.body)
        queryGetOne = 'SELECT * FROM doctor WHERE doctor_id = %s'
        doctorRaw = Doctors.objects.raw(queryGetOne, [val])
        if doctorRaw.__len__() == 0:
            return HttpResponse('Doctor not found')
        result = myCustomSql(json_data, val)
        print('result type:')
        print(type(result))
        print('RESULT: ')
        print(result)
        data = transformer.arraySingleTransform(result)
        print('data')
        print(data)
        return HttpResponse(json.dumps(data))

def myCustomSql(request, doctor_id):
    queryUpdate = """UPDATE doctor SET firstname =%s,middlename= %s, lastname = %s,mobilenumber = %s, gender = %s,address1 = %s, address2 = %s, state = %s, city = %s, zipcode = %s,birthplace = %s, birthday = %s, nik = %s, specialization = %s,certificate = %s, datecertification = %s, countpatientnumber = %s WHERE doctor_id = %s"""
    val = (
        request['firstname'],request['middlename'],request['lastname'],request['mobilenumber'], request['gender'], request['address1'], request['address2'],
        request['state'],request['city'],request['zipcode'],request['birthplace'], request['birthday'], request['nik'], request['specialization'], request['certificate'],
        request['datecertification'],request['countpatientnumber'],
        doctor_id)
    queryGetOne = """SELECT * FROM doctor WHERE doctor_id = %s"""
    with connection.cursor() as cursor:
        cursor.execute(queryUpdate, val)
        row  = cursor.execute(queryGetOne, [doctor_id])
        row = cursor.fetchone()
    return row
