from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from RestApp.models import Employees
from RestApp.serializers import EmployeesSerializer

# Create your views here.

class EmployeeList(APIView):

    def get(self, request):
        Employee1 = Employees.objects.all()
        serializer = EmployeesSerializer(Employee1, many=True)
        return Response(serializer.data)

    def post(self):
        pass

