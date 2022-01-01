from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import LifeInsuranceSerializer
# Create your views here.


class LifeInsuranceView(APIView):
    """
        this view handles the creating life insurance api.
        request must be authenticated.
        if it's not valid it returns 400 and if it's okay returns 201
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = LifeInsuranceSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            insurance = serializer.save()
            if insurance:
                json = serializer.data
                return Response(json, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)