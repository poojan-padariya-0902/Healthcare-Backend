from django.urls import path, include
from rest_framework import routers
from .views import *

urlpatterns = [

    path('api/auth/register/', RegisterViewSet.as_view({'post': 'create'}), name='register'),
    path('api/auth/login/', LoginViewSet.as_view({'post': 'create'}), name='login'),
    
    path('api/patients/', PatientViewSet.as_view({'post': 'create'}), name='create_patient'),
    path('api/patients_list/', PatientViewSet.as_view({'get': 'list'}), name='list_patients'),
    path('api/patient/<int:pk>/', PatientViewSet.as_view({'get': 'retrieve'}), name='get_patient'),
    path('api/patients/<int:pk>/', PatientViewSet.as_view({'put': 'update', 'delete': 'destroy'}), name='update_patient'),
    
    path('api/doctors/', DoctorViewSet.as_view({'post': 'create'}), name='create_doctor'),
    path('api/doctors_list/', DoctorViewSet.as_view({'get': 'list'}), name='list_doctors'),
    path('api/doctor/<int:pk>/', DoctorViewSet.as_view({'get': 'retrieve'}), name='get_doctor'),
    path('api/doctors/<int:pk>/', DoctorViewSet.as_view({'put': 'update', 'delete': 'destroy'}), name='update_doctor'),
    
    path('api/appointments/', AppointmentViewSet.as_view({'post': 'create'}), name='create_appointment'),
    path('api/appointments_list/', AppointmentViewSet.as_view({'get': 'list'}), name='list_appointments'),
    path('api/appointment/<int:pk>/', AppointmentViewSet.as_view({'get': 'retrieve'}), name='get_appointmenr'),
    path('api/appointments/<int:pk>/', AppointmentViewSet.as_view({'put': 'update', 'delete': 'destroy'}), name='update_appointment'),
    
]
