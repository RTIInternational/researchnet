from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import Http404

from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import permissions


from .serializers import UserSerializer, SubmissionSerializer, ConsentSerializer
from .models import Submission, Consent


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


class SubmissionList(APIView):
    """
    List all submissions, or create a new submission.
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        submission = Submission.objects.all()
        serializer = SubmissionSerializer(submission, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubmissionDetail(APIView):
    """
    Retrieve, update or delete a submission instance.
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Submission.objects.get(pk=pk)
        except Submission.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        submission = self.get_object(pk)
        serializer = SubmissionSerializer(submission, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        submission = self.get_object(pk)
        serializer = SubmissionSerializer(submission, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConsentList(APIView):
    """
    Create a consent record
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Consent.objects.get(pk=pk)
        except Consent.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        serializer = ConsentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class ConsentDetail(APIView):
    """
    Update a consent record
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Consent.objects.get(pk=pk)
        except Consent.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        consent = self.get_object(pk)
        serializer = ConsentSerializer(consent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

