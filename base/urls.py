from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [
    path('', views.home, name = 'home'),
    path('contact/', views.contact, name = 'contact'),
    path('about/', views.about, name = 'about'),
    path('auth/login/', obtain_auth_token, name='login'),
    path("auth/logout_user/", views.logout_user, name="logout_user"),
    path("auth/register/", views.user_register_view, name="register"),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]