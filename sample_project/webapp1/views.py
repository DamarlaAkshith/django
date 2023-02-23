from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees
from . serializers import employeesSerializer
# Create your views here.

def add_emp(request):
    if request.method=='POST':
        f_name=request.POST.get('firstname')
        l_name=request.POST.get('lastname')
        emp_id=request.POST.get('emp_id')
        emp=employees(fname=f_name,lname=l_name,emp_id=emp_id)
        emp.save()
        print('emp details added')
        #return HttpRespone("sucess")
        return render(request,'result.html')
    return render(request,'emp.html')

    #user=User.objects.create_user(fname=f_name,lname=l_name,emp_id=emp_id)
    #user.save()
    #print('user created')


class employeeList(APIView):
    def get(self,request):
        employees1=employees.objects.all()
        serializer=employeesSerializer(employees1,many=True)
        return Response(serializer.data)
    def post(self):
        pass
  