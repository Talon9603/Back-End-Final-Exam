from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from django_filters.rest_framework import DjangoFilterBackend

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ['department', 'date_of_joining']
