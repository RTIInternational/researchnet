from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from core.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class EnrollmentsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows acccess to the current enrollments.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer



def logout(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            print("User is valid, active and authenticated")
        else:
            print("inactive users")
    else:
        print("invalid login")

