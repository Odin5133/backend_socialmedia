from rest_framework.viewsets import ModelViewSet
from ..models import loginInfo
from .serializers import loginInfoSerializer, signupSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class LoginInfoViewSet(ModelViewSet):
    queryset=loginInfo.objects.all()
    serializer_class=loginInfoSerializer # what's the purpose of this class?

@api_view(['POST'])
def verify(request):
    if(request.method == 'POST'):
        serializer = loginInfoSerializer(data=request.data)
        if serializer.is_valid():
            user = request.data.get('username')
            userobj = None
            userobj = loginInfo.objects.filter(username=user).first()
            if userobj is not None: 
                passw = request.data.get('password')
                if userobj.password == passw:
                    return Response({'message': 'success'}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'incorrectPassword'}, status=status.HTTP_200_OK)
            return Response({'message': 'userNotFound'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status= status.HTTP_405_METHOD_NOT_ALLOWED)
    # return Response({'message': 'Incorrect Password'}, status=status.HTTP_400_BAD_REQUEST)
    #     return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def signup(request):
    if(request.method == 'POST'):
        serializer = signupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'userCreated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status= status.HTTP_405_METHOD_NOT_ALLOWED)
