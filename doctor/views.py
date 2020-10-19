from django.shortcuts import render
from django.http import HttpResponse
from .models import Doctors
from django.core import serializers

from . import transformer
from django_api.response import Response


# Create your views here.

def index(request):
    # data = serializers.serialize("json", Doctors.objects.all())
    # return HttpResponse(data)
    doctors = Doctors.objects.all()
    doctors = transformer.transform(doctors)
    return Response.ok(values= doctors)



def getOneDoctor(request, doctor_id):
    query = 'SELECT *  FROM doctor WHERE doctor_id = %s'
    val = doctor_id
    data = serializers.serialize('json', Doctors.objects.raw(query, [val]))
    # return HttpResponse('ini doctor_id: %s' % doctor_id)
    return HttpResponse(data)