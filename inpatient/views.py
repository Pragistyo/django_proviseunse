from django.shortcuts import render
from django.http import HttpResponse
from .models import Inpatients
from django.core import serializers

# Create your views here.

def index(request):
    data = serializers.serialize("json", Inpatients.objects.all())
    return HttpResponse(data)
