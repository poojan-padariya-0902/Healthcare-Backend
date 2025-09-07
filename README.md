# 🏥 Healthcare Backend

A backend system for managing **patients, doctors, and appointments** built with **Django** and **Django REST Framework (DRF)**.  
This project provides secure authentication, CRUD operations for healthcare management.

---

## ✨ Features

- 👤 **Authentication & Authorization**
  - User registration & login
  - JWT-based token authentication

- 🧑‍⚕️ **Doctor & Patient Management**
  - Add, update, delete doctors & patients
  - Retrieve lists & individual records

- 📅 **Appointments**
  - Map patients with assigned doctors
  - Manage relationships with CRUD oprations
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

```
Healthcare-Backend/
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
```

---

## ⚙️ Installation & Setup

1. **Clone the repo**
   ```bash
     git clone https://github.com/poojan-padariya-0902/Healthcare-Backend.git
     cd Healthcare-Backend
   ```

2. **Create virtual environment**
   ```bash
     python -m venv venv
     source venv/bin/activate   # For Linux/Mac
     venv\Scripts\activate      # For Windows

3. **Install dependencies**
   ```bash
     pip install -r requirements.txt

4. **Apply migrations**
   ```bash
     python manage.py migrate
   
5. **Run development server**
   ```bash
     python manage.py runserver

Server will start at:
  ```bash
    http://127.0.0.1:8000/
  ```

🔑 Authentication

Register: POST /api/auth/register

Login: POST /api/auth/login (returns JWT token)

Use Authorization: Bearer <token> in headers for secured endpoints.

📌 API Endpoints (Sample)

Patients

POST /api/patients/ → Create new patient

GET /api/patients/ → List all patients

GET /api/patient/{id} → Get Single Record

PUT /api/patients/{id}/ → Update patient

DELETE /api/patients/{id}/ → Delete patient

Doctors

POST /api/doctors/ → Add new doctor

GET /api/doctors/ → List all doctors

GET /api/doctor/{id} → Get Single Record

PUT /api/doctors/{id}/ → Update doctor details

DELETE /api/doctors/{id}/ → Delete doctor

Appointments

POST /api/appointments/ → Book appointment

GET /api/appointments/ → List all appointments

GET /api/appointment/{id} → Get single record

PUT /api/appointments/{id} → Update appointment

DELETE /api/appointments/{id} → Delete Appointment

👨‍💻 Author

Poojan Padariya

[Healthcare-Backend Repository](https://github.com/poojan-padariya-0902/Healthcare-Backend)





