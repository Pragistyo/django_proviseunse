from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:doctor_id>/', views.getOneDoctor, name='detail_doctor'),
]