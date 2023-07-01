from rest_framework import serializers
from hospital.models import Employee, Department, Apointment

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Employee
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Department
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Apointment
        fields = '__all__'

class AnemiaSerializer(serializers.Serializer):
    sex = serializers.IntegerField()
    red_blood_cell = serializers.FloatField()
    white_blood_cell = serializers.FloatField()
    platelets = serializers.FloatField()
    hemoglobin = serializers.FloatField()

    def validate(self, data):

        return data
    
class DiabetesSerializer(serializers.Serializer):
    fasting = serializers.FloatField()
    after_eating = serializers.FloatField()
    hours_after_eating = serializers.FloatField()

    def validate(self, data):
        return data

class KidneySerializer(serializers.Serializer):
    creatinin = serializers.FloatField()
    creatinin_clearance = serializers.FloatField()
    na = serializers.FloatField()
    k = serializers.FloatField()
    cl = serializers.FloatField()
    blood_urine_nitrogen = serializers.FloatField()
    urea = serializers.FloatField()

    def validate(self, data):
        return data

class SurgicalOperationSerializer(serializers.Serializer):
    hemoglopen = serializers.FloatField()
    white_blood = serializers.FloatField()
    platelets = serializers.FloatField()
    liver = serializers.FloatField()
    kidney = serializers.FloatField()
    fluidity = serializers.FloatField()

    def validate(self, data):
        # Perform additional validation if required
        return data



