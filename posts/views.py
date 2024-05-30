from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def add_post(request):
    if request.method == 'POST':
        postForm = forms.PostForm(request.POST)
        if postForm.is_valid():
            postForm.save()
            return redirect('add_post')
    else:
        postForm = forms.PostForm()
    return render(request,'add_post.html',{'form' : postForm})
def edit_post(request,id):
    post = models.Post.objects.get(pk = id)
    postForm = forms.PostForm(instance=post)
    print(post)
    if request.method == 'POST':
        postForm = forms.PostForm(request.POST,instance=post)
        if postForm.is_valid():
            postForm.save()
            return redirect('homepage')
    # else:
    #     postForm = forms.PostForm()
    return render(request,'add_post.html',{'form' : postForm})

def delete_post(request,id):
    post = models.Post.objects.get(pk = id)
    post.delete()
    return redirect('homepage')
  
