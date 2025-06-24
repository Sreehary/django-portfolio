from django.shortcuts import render
from .models import ProfileInfo

def home(request):
    profile = ProfileInfo.objects.all()
    return render(request, 'home.html', {'info': profile[0]})



def education(request):
    profile = ProfileInfo.objects.filter(first_name="Sreehary").first()
    return render(request, 'education.html', {'info': profile})