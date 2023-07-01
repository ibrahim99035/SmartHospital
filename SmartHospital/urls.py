from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hospital/', include('hospital.urls')), 
    path('', include('base.urls')),
]
