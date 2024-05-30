from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_profile(request):
    if request.method == 'POST':
        profileForm = forms.ProfileForm(request.POST)
        if profileForm.is_valid():
            profileForm.save()
            return redirect('add_profile')
    else:
        profileForm = forms.ProfileForm()
    return render(request,'add_profile.html',{'form' : profileForm})

