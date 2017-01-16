from django.shortcuts import render
from profiles.models import Profile

def index(request):
    return render(request, 'index.html')

def show(request, profile_id):

    profile = Profile()

    if profile_id == '1':
        profile = Profile('Lucio', 'luciomoraes@gmail.com', '8215335','My own')
    if profile_id == '2':
        profile = Profile('Suzana', 'suzana@gmail.com', '8215335','Her own')
    return render(request, 'profile.html', {"profile" : profile})