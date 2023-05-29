from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','email']
        
    
    def save(self, **kwargs):
        user = User.objects.create(
            username = self.validated_data['username'],
            password = make_password(self.validated_data['password'])
        )
        result = [{
            'username' : user.username,
            'password': user.password,
            'email':user.email
            }]
        return result