# Back-End-Final-Exam

# Employment Management System
A backend-driven Employee Management System built with Django, Django REST Framework, and PostgreSQL. This project exposes API endpoints for managing employees, departments, attendance, and performance data. It also includes authentication, filtering, pagination, and optional chart visualizations.

## Features
- Modular Django apps: employees, departments, attendance, performance
- PostgreSQL database
- Seed data with Faker
- API Endpoints (CRUD, filtering, pagination)
- JWT Authentication
- Swagger documentation
- Chart visualizations (Optional Bonus)

## Getting Started
### 1. Clone the Repository
```
git clone https://github.com/yourusername/employee_project.git
cd employee_project
```
### 2. Create Environment Variables
Create a .env file:
```
cp .env.example .env
```
### 3. Install Dependencies
```
pip install -r requirements.txt
```
### 4. Run Migrations and Seed Data
```
python manage.py migrate
python manage.py seed_data
```
### 5. Run the Server
```
python manage.py runserver
```

## Swagger Documentation
Available at: /swagger/
- Auto-generated from viewsets
- Supports Try-it-out for requests
- Includes schema info, models, fields, and descriptions


## API Usage Guide
