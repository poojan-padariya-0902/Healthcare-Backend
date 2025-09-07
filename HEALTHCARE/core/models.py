from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Patient(models.Model):
    
    creater = models.ForeignKey(User, related_name='patients', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    address = models.TextField()
    contact = models.CharField(max_length=20)
    medical_history = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Doctor(models.Model):
    
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    
    patient = models.ForeignKey(Patient, related_name='appointments', on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name='appointments', on_delete=models.CASCADE)
    appointment_date = models.DateField()
    reson = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Appointment of {self.patient.name} with {self.doctor.name} on {self.appointment_date}.'