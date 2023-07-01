from django.shortcuts import render
from base.team import Team
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import UserRegisterSerializer
# from rest_framework_simplejwt.tokens import RefreshToken

def home(request):
    title = 'Home'
    isHospital = False
    return render(request, 'home.html', {'title': title, 'isHospital': isHospital})

def contact(request):
    title = 'Contact Us'
    isHospital = False
    return render(request, 'contact.html', {'title': title, 'isHospital': isHospital})

def about(request):
    title = 'About Us'
    isHospital = False
    teamObj = Team()
    teamData = teamObj.getTeamData()
    key1 = [1,2,3,4,5,6,7,8,9,10]
    key2 = [0,1,2,3,4,5]
    return render(request, 'about.html', {'title': title, 'team': teamData, 'key1': key1, 'key2': key2, 'isHospital': isHospital})

@api_view(["POST",])
def logout_user(request):
    if request.method == "POST":
        request.user.auth_token.delete()
        return Response({"Message": "You are logged out"}, status=status.HTTP_200_OK)

@api_view(["POST",])
def user_register_view(request):
    if request.method == "POST":
        serializer = UserRegisterSerializer(data=request.data)
        
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            
            data['response'] = 'Account has been created'
            data['username'] = account.username
            data['email'] = account.email
            
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)
