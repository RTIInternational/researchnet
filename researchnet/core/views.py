from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from core.serializers import UserSerializer, SubmissionSerializer
from .models import Submission


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class SubmissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows acccess to the current enrollments.
    """
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer




