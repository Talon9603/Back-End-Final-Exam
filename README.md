# Back-End-Final-Exam
**Base URL:** https://back-end-final-exam.onrender.com/

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
### Get Access Token
```
POST /api/token/
```

### Request Body
```
{
  "username": "your_username",
  "password": "your_password"
}
```

### Response
```
{
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token"
}
```

### Refresh Token
```
POST /api/token/refresh/
```

### Request Body (JSON)
```
{
  "refresh": "your_refresh_token"
}
```

### CRUD Endpoints
```
Authorization: Bearer your_access_token
```
#### Employees
- ```GET /api/employees/``` – List employees
- ```POST /api/employees/``` – Create employee
- ```GET /api/employees/{id}/``` – Retrieve single employee
- ```PUT /api/employees/{id}/``` – Update employee
- ```DELETE /api/employees/{id}/``` – Delete employee

#### Departments
- ```GET /api/departments/``` – List departments
- ```POST /api/departments/``` – Create departments
- ```GET /api/departments/{id}/``` – Retrieve single department
- ```PUT /api/departments/{id}/``` – Update departments
- ```DELETE /api/departments/{id}/``` – Delete departments

#### Attendance
- ```GET /api/attendance/``` – List attendance
- ```POST /api/attendance/``` – Create attendance
- ```GET /api/attendance/{id}/``` – Retrieve single attendance
- ```PUT /api/attendance/{id}/``` – Update attendance
- ```DELETE /api/attendance/{id}/``` – Delete attendance

#### Performance
- ```GET /api/performance/``` – List performance
- ```POST /api/performance/``` – Create performance
- ```GET /api/performance/{id}/``` – Retrieve single performance
- ```PUT /api/performance/{id}/``` – Update performance
- ```DELETE /api/performance/{id}/``` – Delete performance
