from django.contrib import admin
from hospital.models import Employee, Department, Diagnose, Patient



admin.site.register(Employee)
admin.site.register(Diagnose)
admin.site.register(Department)
admin.site.register(Patient)