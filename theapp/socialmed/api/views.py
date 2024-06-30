from rest_framework.viewsets import ModelViewSet
from ..models import loginInfo
from .serializers import loginInfoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class LoginInfoViewSet(ModelViewSet):
    queryset=loginInfo.objects.all()
    serializer_class=loginInfoSerializer

@api_view(['POST'])
def verify(request):
    if(request.method == 'POST'):
        user = request.data.get('username')
        userobj = None
        if user is not None:
            userobj = loginInfo.objects.filter(username=user).first()
            passw = request.data.get('password')
            if userobj.password == passw:
                return Response({'message': 'Success'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Incorrect Password'}, status=status.HTTP_200_OK)
        return Response({'message': 'User not found'}, status=status.HTTP_200_OK)
    
    # return Response({'message': 'Incorrect Password'}, status=status.HTTP_400_BAD_REQUEST)
    #     return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

