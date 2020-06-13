from django.shortcuts import render
from django.http import HttpResponse
from .models import PersonalInfo

# Create your views here.

def index(request):
    personalInfo = PersonalInfo.objects.all()
    return render(request, 'index.html', {'info': personalInfo})
