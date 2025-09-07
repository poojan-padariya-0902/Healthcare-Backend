from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from .models import *
from .serializers import *
from .permissions import IsOwner

# Create your views here.

class RegisterViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
        )
        user.save()
        
        serializer = RegisterSerializer(user)
        data = serializer.data
        
        return Response({
            'status': 'success',
            'message': 'User registered successfully.',
            'data': data
        })
    
class LoginViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = User.objects.filter(username=username).first()
        
        if user is None:
            return Response({
                'status': 'faild',
                'message': 'User note found.',
            })
        user = authenticate(username=username, password=password)
        if not user:
            return Response({
                'status': 'faild',
                'message': 'Incorrect Password.'
            })
        login(request, user)
        
        access_token = AccessToken.for_user(user)
        refresh_token = RefreshToken.for_user(user)
        
        serializer = LoginSerializer(user)
        data = serializer.data
        data['access_token'] = str(access_token)
        data['refresh_token'] = str(refresh_token)
        
        return Response({
            'status': 'success',
            'message': 'User logged in successfully.',
            'data': data
        })
        
class PatientViewSet(viewsets.ModelViewSet):
    
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    
    def create(self, request, *args, **kwargs):
        
        name = request.data.get('name')
        age = request.data.get('age')
        address = request.data.get('address')
        contact = request.data.get('contact')
        medical_history = request.data.get('medical_history')
        
        patient = Patient.objects.create(
            creater = request.user,
            name=name,
            age=age,
            address=address,
            contact=contact,
            medical_history=medical_history,
        )
        patient.save()
        
        serializer = PatientSerializer(patient)
        data = serializer.data
        
        return Response({
            'status': 'success',
            'message': 'Patient record created successfully.',
            'data': data
        })
        
    def list(self,request, *args, **kwargs):
            
        patients = Patient.objects.filter(creater=request.user)
        serializer = PatientSerializer(patients, many=True)
        data = serializer.data
        
        for record in data:
            if 'creater' in record:
                del record['creater']
        
        return Response({
            'status': 'success',
            'message': 'Patient records fetched successfully.',
            'data': data
        })
        
    def retrieve(self, request, *args, **kwargs):
        
        patient = self.get_object()
        serializer = PatientSerializer(patient)
        data = serializer.data
        
        data.pop('creater', None)
                
        return Response({
            'status': 'success',
            'message': 'Patient record fetched successfully.',
            'data': data
        })
        
    def update(self, request, *args, **kwargs):
        
        patient = self.get_object()
        
        serializer = PatientSerializer(patient, data=request.data, partial=True)
        
        if serializer.is_valid():
            
            serializer.save()
            data = serializer.data
            data.pop('creater', None)
            
            return Response({
                'status': 'success',
                'message': 'Patient record updated successfully.',
                'data': data
            })
        return Response({
            'status': 'faild',
            'message': 'Something went wrong.',
            'errors': serializer.errors
        })
        
    def destroy(self, request, *args, **kwargs):
        
        patient = self.get_object()
        
        if patient is None:
            return Response({
                'status': 'faild',
                'message': 'Patient record not found.'
            })
        patient.delete()
        
        return Response({
            'status': 'success',
            'message': 'Patient record deleted successfully.'
        })
        
class DoctorViewSet(viewsets.ModelViewSet):
    
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        
        serializer = DoctorSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response({
                'status': 'faild',
                'message': 'Something went wrong.',
                'errors': serializer.errors
            })
        serializer.save()
        data = serializer.data
        
        return Response({
            'status': 'success',
            'message': 'Doctor record created successfully.',
            'data': data
        })
        
    def list(self, request, *args, **kwargs):
        
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        data = serializer.data
        
        return Response({
            'status': 'success',
            'message': 'Doctor records fetched successfully.',
            'data': data
        })
        
    def retrieve(self, request, *args, **kwargs):
        
        doctor = self.get_object()
        serializer = DoctorSerializer(doctor)
        data = serializer.data
        
        return Response({
            'status': 'success',
            'message': 'Doctor record fetched successfully.',
            'data': data
        })
    
    def update(self, request, *args, **kwargs):
        
        doctor = self.get_object()
        serializer = DoctorSerializer(doctor, data=request.data, partial=True)
        
        if not serializer.is_valid():
            return Response({
                'status': 'faild',
                'message': 'Something went wrong.',
                'errors': serializer.errors
            })
        serializer.save()
        data = serializer.data
        
        return Response({
            'status': 'success',
            'message': 'Doctor record updated successfully.',
            'data': data
        })
    def destroy(self, request, *args, **kwargs):
        
        doctor = self.get_object()
        
        if doctor is None:
            return Response({
                'status': 'faild',
                'message': 'Doctor record not found.'
            })
        doctor.delete()
        return Response({
            'status': 'success',
            'message': 'Doctor record deleted successfully.'
        })
        
class AppointmentViewSet(viewsets.ModelViewSet):
    
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        
        serializer = AppointmentSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response({
                'status': 'faild',
                'message': 'Something went wrong.',
                'errors': serializer.errors
            })
        serializer.save()
        data = serializer.data
        
        return Response({
            'status': 'success',
            'message': 'Appointment record created successfully.',
            'data': data
        })
    
    def list(self, request, *args, **kwargs):
        
        appointment = Appointment.objects.all()
        serializer = AppointmentSerializer(appointment, many=True)
        data = serializer.data
        
        return Response({
            'status': 'success',
            'message': 'Appointment records created successfully.',
            'data': data
        })
        
    def retrieve(self, request, *args, **kwargs):
        
        appointment = self.get_object()
        serializer = AppointmentSerializer(appointment)
        data = serializer.data
        
        return Response({
            'status': 'success',
            'message': 'Appointmnet record fetched successfully.',
            'data': data
        })
        
    def update(self, request, *args, **kwargs):
        
        appointment = self.get_object()
        serializer = AppointmentSerializer(appointment, data=request.data, partial=True)
        
        if not serializer.is_valid():
            return Response({
                'status': 'faild',
                'message': 'Something went wrong.',
                'errors': serializer.errors
            })
        serializer.save()
        data = serializer.data
        
        return Response({
            'status': 'success',
            'message': 'Appointment record updated successfully.',
            'data': data
        })
        
    def destroy(self, request, *args, **kwargs):
        
        appointment = self.get_object()
        
        if appointment is None:
            return Response({
                'status': 'faild',
                'message': 'Apointment record not found.'
            })
        appointment.delete()
        return Response({
            'status': 'success',
            'message': 'Appointment record deleted successfully.'
        })