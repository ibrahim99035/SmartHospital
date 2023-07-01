from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.http import JsonResponse
import os
from rest_framework.response import Response
from rest_framework.decorators import api_view
from hospital.models import Employee, Department, Apointment
from hospital.serializers import EmployeeSerializer, DepartmentSerializer, SurgicalOperationSerializer, AnemiaSerializer, DiabetesSerializer, KidneySerializer, AppointmentSerializer
from hospital.medical import Anemia, Diabetes, Kidney, SurigcalOperation

def hospital(request):
    title = 'Diagnosing'
    isHospital = True
    return render(request, 'hospital.html', {'title': title, 'isHospital': isHospital})

#Diagnosing Functionality
def braintumor(request):
    title = 'Brain Tumor'
    result = ''
    isHospital = True

    return render(request, 'braintumor.html', {'title': title, 'result': result, 'isHospital': isHospital})

def breastcancer(request):
    isHospital = True
    title = 'Brast Cancer'
    return render(request, 'breastcancer.html', {'title': title, 'isHospital': isHospital})

@api_view(['GET'])
def getEmployees(request):
    Employees = Employee.objects.all()
    serializer = EmployeeSerializer(Employees, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def postEmployee(request):
    serializer = EmployeeSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def getDepartments(request):
    Departments = Department.objects.all()
    serializer = DepartmentSerializer(Departments, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def postDepartment(request):
    serializer = DepartmentSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def appointment(request):
    appointments = Apointment.objects.all()  # Assuming the model name is "Appointment"
    serializer = AppointmentSerializer(data=request.data)
    
    if serializer.is_valid():
        doctor = serializer.validated_data.get('doctor')
        date = serializer.validated_data.get('date')
        already_booked = Apointment.objects.filter(doctor=doctor, date=date).exists()
        
        if already_booked:
            return Response({'message': 'This session is already booked'})
        else:
            serializer.save()
            return Response({'message': 'Session booked successfully'})
    
    return Response(serializer.errors)


@api_view(['POST'])
def checkAnemia(request):
    serializer = AnemiaSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    validated_data = serializer.validated_data
    anemia_instance = Anemia()
    result = anemia_instance.checkAnemia(
        Sex=validated_data['sex'],
        Red_Blood_Cell=validated_data['red_blood_cell'],
        White_Blood_Cell=validated_data['white_blood_cell'],
        Platelets=validated_data['platelets'],
        Hemoglobin=validated_data['hemoglobin']
    )

    return Response({'result': result})

@api_view(['POST'])
def checkDiabetes(request):
    serializer = DiabetesSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    validated_data = serializer.validated_data

    diabetes_instance = Diabetes()
    result = diabetes_instance.checkTheCase(
        Fasting=validated_data['fasting'],
        After_Eating=validated_data['after_eating'],
        Hours_After_Eating=validated_data['hours_after_eating']
    )

    return Response({'result': result})

@api_view(['POST'])
def checkKideny(request):
    serializer = KidneySerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    # Extract validated data
    validated_data = serializer.validated_data

    # Create an instance of the Kidney class and call the checkKidney method
    kidney_instance = Kidney()
    result = kidney_instance.checkKidney(
        Creatinin=validated_data['creatinin'],
        Creatinin_Clearance=validated_data['creatinin_clearance'],
        Na=validated_data['na'],
        K=validated_data['k'],
        Cl=validated_data['cl'],
        Blood_Urine_Nitrogen=validated_data['blood_urine_nitrogen'],
        Urea=validated_data['urea']
    )

    return Response({'result': result})

@api_view(['POST'])
def checkSurgical(request):
    serializer = SurgicalOperationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    validated_data = serializer.validated_data

    surgical_operation_instance = SurigcalOperation()
    result = surgical_operation_instance.checkpatientResult(
        hemoglopen=validated_data['hemoglopen'],
        whiteBlood=validated_data['white_blood'],
        platelets=validated_data['platelets'],
        liver=validated_data['liver'],
        kidney=validated_data['kidney'],
        fluidity=validated_data['fluidity']
    )

    return Response({'result': result})