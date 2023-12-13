from django.shortcuts import render
from .models import personalProfile

def profile(req):
    db =   personalProfile.objects.all()
    context = {'db':db}
    return render(req, 'myprofile/profile.html', context)