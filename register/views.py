from rest_framework import status, views
from rest_framework.response import Response
from .serializers import UserRegisterSerializer, UserAuthSerializer, UserConfirmSerializer

class UserRegisterView(views.APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "Пользователь успешно зарегистрирован. Пожалуйста, подтвердите свой email."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAuthView(views.APIView):
    def post(self, request):
        serializer = UserAuthSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserConfirmView(views.APIView):
    def post(self, request):
        serializer = UserConfirmSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
