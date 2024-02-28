from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.permissions import BasePermission
from rest_framework import filters, pagination
# Create your views here.

class DoctorViewset(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer
    
class SpecializationViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer
    
class DesignationViewset(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer
    

    
class AvailableTimeForSpecific(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        doctor_id=request.query_params.get("doctor_id")
        if doctor_id:
            return queryset.filter(doctor= doctor_id)
        return queryset
    
class AvailableTimeViewset(viewsets.ModelViewSet):
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends= [AvailableTimeForSpecific]
    

    
class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    
