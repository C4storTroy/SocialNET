from django.shortcuts import render, redirect
from profiles.models import Profile

def index(request):
    return render(request, 'index.html', {'profiles' : Profile.objects.all()})

def show(request, profile_id):

    profile = Profile.objects.get(id=profile_id)
    return render(request, 'profile.html', {"profile" : profile})

def invite(request, profile_id):
    profile_to_invite = Profile.objects.get(id=profile_id)
    profile_logged = get_profile_logged(request)
    profile_logged.invite(profile_to_invite)
    return redirect('index')

'''for now just Profile with id=1 will be logged'''
def get_profile_logged(request):
    return Profile.objects.get(id=1)