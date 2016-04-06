import logging

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import Http404
from django.core.mail import send_mail
from django.template import loader


from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import permissions
from .permissions import IsStaffOrTargetUser

from .serializers import UserSerializer, SubmissionSerializer, ConsentSerializer, ParticipantSerializer
from .models import Submission, Consent, Participant


logger = logging.getLogger(__name__)

class UserViewSet(viewsets.ModelViewSet):
    
    permission_classes = (permissions.IsAuthenticated,)

    """
    API endpoint that allows users to be viewed.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def get_permissions(self):
        # allow non-authenticated user to create via POST
        return (permissions.AllowAny() if self.request.method == 'POST'
                else IsStaffOrTargetUser()),


class SubmissionViewSet(viewsets.ModelViewSet):
    
    permission_classes = (permissions.IsAuthenticated,)
    
    """
    API endpoint that allows acccess to the current submission.
    """
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer


class SubmissionList(APIView):
    """
    List all submissions, or create a new submission
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        submission = Submission.objects.all()
        serializer = SubmissionSerializer(submission, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        
        serializer = SubmissionSerializer(data=request.data, context={'request': self.request})

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubmissionDetail(APIView):
    """
    Retrieve or update a submission
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


class ParticipantList(APIView):
    """
    List all participants, or create a new participant
    """
    def get(self, request, format=None):
        participant = Participant.objects.all()
        serializer = ParticipantSerializer(participant, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ParticipantSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            participant = serializer.data
            
        
            html_message = loader.render_to_string(
            'welcome_email.html',
            {
                'first_name': participant['first_name'],
                'last_name': participant['last_name']
            })

            # possibly put a check here to make sure this is a valid email address
            send_mail('Welcome to RTI\'s Researchnet', 'Here is the message.', 'researchnet@ictedge.org', [participant['email']], fail_silently=True,html_message=html_message)
    
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ParticipantDetail(APIView):
    """
    Update a study participant
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Participant.objects.get(pk=pk)
        except Participant.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        participant = self.get_object(pk)
        serializer = ParticipantSerializer(consent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def HeartBeat(request):
    """
    This method is for the AWS load balancer health check.
    """
    return HttpResponse('{\'data\': {\'status\': \'healthy\'}}')
