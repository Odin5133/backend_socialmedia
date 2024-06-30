from rest_framework.serializers import ModelSerializer
from ..models import loginInfo

class loginInfoSerializer(ModelSerializer):
    class Meta:
        model = loginInfo
        fields = ('username', 'password')