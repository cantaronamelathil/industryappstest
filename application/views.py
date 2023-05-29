from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login,logout,authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated



def get_token_for_user(user):
    refresh=RefreshToken.for_user(user)
    
    return{
        'refresh':str(refresh),
        'access':str(refresh.access_token)
    }
    



class CustomLogin(APIView):
    '''
    
    '''
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username,password)
        user = authenticate(username=username,password=password)
        if user is not None:
            token = get_token_for_user(user=user)
            login(request=request,user=user)
            return Response({'msg':'successfully logind','token':token})
        return Response({'msg':'custom login','required fields':['username','password']})
    
    
    
    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response({'msg':'logout successfully'})

        
    
class Home(APIView):
    '''
    
    '''
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        userlist = User.objects.all()
        if userlist is not None:
            serializer = UserSerializer(userlist,many=True)
            return Response({'msg':'success','data':serializer.data})
        return Response({'msg':'database have no data'})
    


class SignUp(APIView):
    '''
    
    '''
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'msg':'successfully signup','data':serializer.data})