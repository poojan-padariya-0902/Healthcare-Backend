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

Healthcare-Backend/
│── api/ # Core app (models, serializers, views, urls)
│── healthcare/ # Django project settings & configs
│── requirements.txt # Project dependencies
│── manage.py # Django entry point
