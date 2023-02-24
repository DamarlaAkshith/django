from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees
from . serializers import employeesSerializer
from rest_framework.decorators import api_view

from rest_framework import serializers
# Create your views here.

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_employees': '/',
        'Search by firstname': '/?fname=firstname',
        'Search by lastname': '/?lname=lastname',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
 
    return Response(api_urls)

@api_view(['POST'])
def add_emp(request):
    emp = employeesSerializer(data=request.data)
 
    # validating for already existing data
    if employees.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if emp.is_valid():
        emp.save()
        return Response(emp.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_emps(request):
	if request.query_params:
		emp = employees.objects.filter(**request.query_params.dict())
	else:
		emp = employees.objects.all()
	if emp:
		serializer = employeesSerializer(emp, many=True)
		return Response(serializer.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def update_emp(request, pk):
	item = employees.objects.get(pk=pk)
	data = employeesSerializer(instance=item, data=request.data)

	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['DELETE'])
def delete_emp(request, pk):
	item = get_object_or_404(employees, pk=pk)
	item.delete()
	return Response(status=status.HTTP_202_ACCEPTED)





# def add_emp(request):
#     if request.method=='POST':
#         f_name=request.POST.get('firstname')
#         l_name=request.POST.get('lastname')
#         emp_id=request.POST.get('emp_id')
#         emp=employees(fname=f_name,lname=l_name,emp_id=emp_id)
#         emp.save()
#         print('emp details added')
#         #return HttpRespone("sucess")
#         return render(request,'result.html')
#     return render(request,'emp.html')

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
  