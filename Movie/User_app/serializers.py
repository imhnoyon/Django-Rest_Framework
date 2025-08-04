from rest_framework import serializers
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'})
    class Meta:
        model=User
        fields=['username','email','password','password2']


    def save(self):
        username=self.validated_data['username']
        email=self.validated_data['email']
        password1=self.validated_data['password']
        password2=self.validated_data['password2']

        if password1 != password2:
            raise serializers.ValidationError({'error':"Password doesn't match!!"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error':"Email already Exists.."})
        
        account=User(username=username,email=email)
        account.set_password(password1)
        account.save()
        return account
        