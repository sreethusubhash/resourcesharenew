from typing import Optional
from django.contrib.auth import authenticate
from rest_framework.views import APIView # turn our class to API view
from rest_framework.response import Response # Return JSON
from rest_framework import status # set status code
from rest_framework.authtoken.models import Token # generate token
from . import models
from . import serializers


class UserProfile(APIView):
    def get(self, request):
        #breakpoint()
        user=models.User.objects.prefetch_related('resources_set').get(id=request.user.id)
        response=serializers.UserProfileModelSerializer(user)
        return Response(response.data)
    
class UserLogin(APIView):
    def post(self, request):
        # get credentials
        password = request.data.get('password')
        username = request.data.get('username')
        
        # Authenticate the user
        user:Optional[models.User] = authenticate(
            username = username,
            password = password, )#dict of reqt body
        
        if not user:
            return Response(
                {"error": "Password or Username not correct."},
                status=status.HTTP_404_NOT_FOUND,
            )
            
        # Create Token
        token, _ =Token.objects.get_or_create(user=user)
            
        return Response(
            {"token": token.key},
            status=status.HTTP_201_CREATED
        )










