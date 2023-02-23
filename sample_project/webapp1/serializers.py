from rest_framework import serializers
from . models import employees
#from rest_framework import models

class employeesSerializer(serializers.ModelSerializer):
    class Meta:
        model=employees
        #fields={'fname','lname'}
        fields='__all__'
