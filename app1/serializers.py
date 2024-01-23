from .models import *
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('dept_aid','dept_label','dept_description','activestatus','addedby','adddate','updatedby','updatedate')

