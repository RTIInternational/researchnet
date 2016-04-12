import csv
from core.models import Submission, Participant

from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect
from django.core.mail import send_mail

from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)

from core.forms import ResearchnetAuthForm

# Create your views here.
@login_required
def index(request):
    submissions = Submission.objects.order_by('-timestamp')[:10]
    context = {'submission_list': submissions}
    return render(request, 'index.html', context)


@login_required
def enrollment(request):
    participants = Participant.objects.order_by('-user__date_joined')[:10]
    context = {'participant_list': participants}
    return render(request, 'participant.html', context)

@login_required
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

@login_required
def export_enrollees(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="study_enrollees.csv"'

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Username', 'Email Address', 'Gender', 'DOB'])
    
    participants = Participant.objects.all()
    for participant in participants:
        writer.writerow([participant.user.first_name, participant.user.last_name, participant.user.username, participant.user.email, participant.gender, participant.dob])

    return response


def login_view(request, *args, **kwargs):
    
    redirect_to = request.POST.get(REDIRECT_FIELD_NAME, request.GET.get(REDIRECT_FIELD_NAME, ''))

    if request.method == "POST":
        
        form = ResearchnetAuthForm(request, data=request.POST)

        if form.is_valid():
            print("form is valid")

            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            
            if user is not None :
                
                if user.has_perm('view_dashboard'):
                    login(request, user)
                    return HttpResponseRedirect(redirect_to)
                else:
                    form.add_error(None, "Participant login not supported")
        else:
            print("not valid form")
            form

    else: # not a post
        form = ResearchnetAuthForm(request)

    
    context = {
        'form': form,
        REDIRECT_FIELD_NAME: redirect_to
    }

    return render(request, 'registration/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')

