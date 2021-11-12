from rest_framework.serializers import ModelSerializer
from todo.models import Todo
from django.contrib.auth.models import User
from rest_framework import serializers



class RegistrationSerializer(ModelSerializer):
    class Meta:
        model=User
        fields = ['username','email','password']

    def create(self, validated_data):
        return User.objects.create_user(username=validated_data["username"],
                                        password=validated_data["password"],email=validated_data["email"])



class TodoSerializer(ModelSerializer):
    user=RegistrationSerializer()
    class Meta:
        model= Todo
        fields=['task_name','user','completed']




class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()