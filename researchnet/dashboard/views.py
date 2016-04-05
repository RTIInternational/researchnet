import csv
from django.shortcuts import render
from django.http import HttpResponse
from core.models import Submission, Participant
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.core.mail import send_mail


# Create your views here.
@login_required
def index(request):
    submissions = Submission.objects.order_by('timestamp')[:10]
    context = {'submission_list': submissions}
    return render(request, 'index.html', context)


@login_required
def enrollment(request):
	participants = Participant.objects.all()
	context = {'participant_list': participants}
	return render(request, 'participant.html', context)


def export_submissions(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="study_submisisons.csv"'

    writer = csv.writer(response)
    writer.writerow(['Username', 'Timestamp', 'Device Id', 'Location'])
    
    submissions = Submission.objects.all()

    for submission in submissions:
        writer.writerow([submission.user.username, submission.timestamp, submission.device_id, 'Not Available'])

    return response


def export_enrollees(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="study_enrollees.csv"'

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Username', 'Email Address', 'Gender', 'DOB'])
    
    participants = Participant.objects.all()
    for participant in participants:
        writer.writerow([participant.first_name, participant.last_name, participant.username, participant.email, participant.gender, participant.dob])

    return response


def logout_view(request):
    logout(request)
    return redirect('home')

