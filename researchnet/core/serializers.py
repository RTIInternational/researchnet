from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Submission, Consent, ParticipantUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ParticipantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ParticipantUser
        fields = ( 'gender', 'dob', 'user' )
        depth = 1

class SubmissionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Submission
        fields = ('id','user', 'time_start', 'time_complete', 'timestamp', 'device_id', 'response')

class ConsentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Consent
		fields = ('id', 'user', 'scope', 'consent_date')

