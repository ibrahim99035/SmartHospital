from django.db import models
from django.forms import RadioSelect
from django.utils import timezone

class Department(models.Model):
    name =  models.CharField(max_length=25)
    description = models.CharField(max_length=5000)

class Employee(models.Model):
    Fname = models.CharField(max_length=25)
    Lname = models.CharField(max_length=25)
    username = models.CharField(max_length=30)
    
    ROLE_OPTIONS = (
        ('D', 'Doctor'),
        ('N', 'Nurse'),
    )
    role = models.CharField(max_length=1, choices=ROLE_OPTIONS)
    phone = models.CharField(max_length=25)
    email = models.EmailField()
    nationalID = models.CharField(max_length=14)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class Patient(models.Model):
    Fname = models.CharField(max_length=25)
    Lname = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    email = models.EmailField()
    nationalID = models.CharField(max_length=14)
    medicalHistory = models.TextField(max_length=10000, blank=True)
    admission_data = models.DateTimeField(default=timezone.now)
    staff = models.ManyToManyField(Employee)

class Diagnose(models.Model):
    date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=50)
    result = models.CharField(max_length=500)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

class Apointment(models.Model):
    name = models.CharField(max_length=25)
    doctor = models.CharField(max_length=25)
    date = models.CharField(max_length=5)
