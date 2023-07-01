from django.urls import path
from . import views

urlpatterns = [
    path('', views.hospital, name = 'hospital'), 
    path('braintumor/', views.braintumor, name = 'braintumor'),
    path('breastcancer/', views.breastcancer, name = 'breastcancer'),
    path('api/get_empolyees', views.getEmployees, name = 'Get_Employees'),
    path('api/add_employee', views.postEmployee, name = 'Add_Employee'),
    path('api/get_departments', views.getDepartments, name = 'Get_Departments'),
    path('api/add_department', views.postDepartment, name = 'Add_Department'),
    path('api/appointment', views.appointment, name = 'appointment'),
    path('api/anemia/', views.checkAnemia, name='check_anemia'),
    path('api/diabetes/', views.checkDiabetes, name='check_diabetes'),
    path('api/kidney/', views.checkKideny, name='check_kideny'),
    path('api/surgical/', views.checkSurgical, name='check_surgical'),
]