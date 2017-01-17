from django.shortcuts import render
from profiles.models import Profile

def index(request):
    return render(request, 'index.html', {'profiles' : Profile.objects.all()})

def show(request, profile_id):

    profile = Profile.objects.get(id=profile_id)
    return render(request, 'profile.html', {"profile" : profile})