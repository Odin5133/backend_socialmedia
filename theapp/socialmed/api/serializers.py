from rest_framework import serializers
from ..models import loginInfo
#from rest_framework.validators import UniqueValidator

class loginInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = loginInfo
        fields = ('username', 'password')

class signupSerializer(serializers.Serializer):
    class Meta:
        model = loginInfo
        fields = ('username', 'password')
        extra_kwargs = {
            'username' : {'unique': True},
        }
        