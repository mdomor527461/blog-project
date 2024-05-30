from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_author(request):
    if request.method == 'POST':
        authorForm = forms.AuthorForm(request.POST)
        if authorForm.is_valid():
            authorForm.save()
            return redirect('add_author')
    else:
        authorForm = forms.AuthorForm()
    return render(request,'add_author.html',{'form' : authorForm})
