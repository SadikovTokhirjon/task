from employees.serializers import EmployeeSerializer
from employees.models import Employees
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]