from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'age', 'contact')
    search_fields = ('name', 'contact')
    
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'email', 'contact', 'specialization')
    search_fields = ('name', 'contact')
    
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'appointment_date')
    search_fields = ('patient__name', 'doctor__name')
    