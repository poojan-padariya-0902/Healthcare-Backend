# 🏥 Healthcare Backend

A backend system for managing **patients, doctors, and appointments** built with **Django** and **Django REST Framework (DRF)**.  
This project provides secure authentication, CRUD operations, and role-based access for healthcare management.

---

## ✨ Features

- 👤 **Authentication & Authorization**
  - User registration & login
  - JWT-based token authentication
  - Role-based access control

- 🧑‍⚕️ **Doctor & Patient Management**
  - Add, update, delete doctors & patients
  - Retrieve lists & individual records

- 🔗 **Patient–Doctor Mapping**
  - Map patients with assigned doctors
  - Manage relationships with CRUD operations

- 📅 **Appointments**
  - Book, update, and cancel appointments
  - Track history with timestamps

---

## 🛠️ Tech Stack

- **Backend Framework:** Django 5, Django REST Framework  
- **Database:** SQLite (default) / PostgreSQL (recommended)  
- **Authentication:** JWT (SimpleJWT)  
- **Testing Tools:** Postman / cURL  

---

## 📂 Project Structure

```Healthcare-Backend/
│── core/ # Core Django app
│ │── migrations/ # Database migrations
│ │── init.py
│ │── admin.py # Django admin configuration
│ │── apps.py # App configuration
│ │── models.py # Database models (Patient, Doctor, Appointment)
│ │── serializers.py # DRF serializers
│ │── views.py # API views (CRUD & business logic)
│ │── urls.py # API routes for this app
│ │── permissions.py # Custom permissions (if any)
│
│── HEALTHCARE/ # Django project settings
│ │── init.py
│ │── asgi.py # ASGI entry point
│ │── settings.py # Global project settings
│ │── urls.py # Main URL router
│ │── wsgi.py # WSGI entry point
│── manage.py # Django management script
── requirements.txt # Python dependencies
── README.md # Project documentation



