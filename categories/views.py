from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_category(request):
    if request.method == 'POST':
        cateygoryForm = forms.CategoryForm(request.POST)
        if cateygoryForm.is_valid():
            cateygoryForm.save()
            return redirect('add_category')
    else:
        cateygoryForm = forms.CategoryForm()
    return render(request,'add_category.html',{'form' : cateygoryForm})
