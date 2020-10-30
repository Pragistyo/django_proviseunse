from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:medicalrecord_id>/detail/', views.show, name='detail_medical_record'),
    path('customQuery/getBydatePolyclinic', views.customQuery, name='custom_medical_record'),
]