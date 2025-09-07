from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

# Create your serializers here.

class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email']
        
class LoginSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        
class PatientSerializer(serializers.ModelSerializer):
    
    creater_name = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ['creater', 'updated_at', 'created_at']
        
    def get_creater_name(self, obj):
        creater_name = obj.creater.first_name + ' ' + obj.creater.last_name
        return creater_name
    
class DoctorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Doctor
        fields = '__all__'
        read_only_fields = ['updated_at', 'created_at']
        
class AppointmentSerializer(serializers.ModelSerializer):
    
    patient_name = serializers.SerializerMethodField()
    doctor_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Appointment
        fields = '__all__'
        read_only_fields = ['updated_at', 'created_at']
        
    def get_patient_name(self, obj):
        return obj.patient.name
    
    def get_doctor_name(self, obj):
        return obj.doctor.name