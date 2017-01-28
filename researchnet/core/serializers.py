from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Submission, Consent, Participant
import pdb


class ParticipantUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        
        fields = ('username', 'email', 'password', 'first_name', 'last_name','gender', 'dob')
        
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)
    
    gender=serializers.CharField(source='participant.gender')
    dob=serializers.DateField(source='participant.dob')

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class ParticipantSerializer(serializers.Serializer):
    
    username=serializers.CharField(source='user.username')
    password=serializers.CharField(
        style={'input_type': 'password'}, source='user.password', write_only=True
    )
    first_name=serializers.CharField(source='user.first_name')
    last_name=serializers.CharField(source='user.last_name')
    email=serializers.EmailField(source='user.email')
    gender=serializers.CharField()
    dob=serializers.DateField(required=False, allow_null=True)

    def create(self, validated_data):
            
        user = User(
            username=validated_data['user']['username'],
            first_name=validated_data['user']['first_name'],
            last_name=validated_data['user']['last_name'],
            email=validated_data['user']['email']
        )
        user.set_password(validated_data['user']['password'])
        user.save()

        participant = Participant(user=user, gender=validated_data['gender'],dob=validated_data['dob'])
        participant.save()

        return participant


class SubmissionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Submission
        fields = ('id', 'participant', 'time_start', 'time_complete', 'timestamp', 'device_id', 'response','lat','long', 'place')

    participant = ParticipantUserSerializer(many=False, read_only=True, source='user')

    def create(self, validated_data):
        submission = Submission(**validated_data)
        submission.save()
        return submission



class ConsentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Consent
		fields = ('id', 'user', 'scope', 'consent_date')

