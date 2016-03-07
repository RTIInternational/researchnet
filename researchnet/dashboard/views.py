from django.shortcuts import render
from django.http import HttpResponse
from core.models import Submission
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    submissions = Submission.objects.order_by('timestamp')[:10]
    context = {'submission_list': submissions}
    return render(request, 'index.html', context)

