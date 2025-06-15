from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from django_filters.rest_framework import DjangoFilterBackend

from django.shortcuts import render
from departments.models import Department
from attendance.models import Attendance
from employees.models import Employee
from django.db.models import Count
from datetime import date, timedelta

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ['department', 'date_of_joining']


def chart_view(request):
    # Employees per Department
    dept_qs = Department.objects.annotate(emp_count=Count('employees'))
    dept_data = {
        "labels": [d.name for d in dept_qs],
        "data": [d.emp_count for d in dept_qs],
    }

    # Attendance per Month (last 6 months)
    today = date.today()
    months = [(today.replace(day=1) - timedelta(days=30 * i)).strftime("%B %Y") for i in reversed(range(6))]
    data = []
    for i in reversed(range(6)):
        first = (today.replace(day=1) - timedelta(days=30 * i)).replace(day=1)
        last = (first + timedelta(days=32)).replace(day=1) - timedelta(days=1)
        count = Attendance.objects.filter(date__range=[first, last], status='PRESENT').count()
        data.append(count)

    attendance_data = {
        "labels": months,
        "data": data,
    }

    return render(request, 'charts.html', {
        'dept_data': dept_data,
        'attendance_data': attendance_data,
    })
