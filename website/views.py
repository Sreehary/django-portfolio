from django.shortcuts import render
from .models import ProfileInfo, EducationInfo


def home(request):
    profile = ProfileInfo.objects.all()
    return render(request, 'home.html', {'info': profile[0]})


def education(request):
    educations = EducationInfo.Education.objects.all()
    return render(request, 'education.html', {'educations': educations})
