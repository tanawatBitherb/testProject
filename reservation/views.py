from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('posts:list')
    else:
        form = UserCreationForm()
    return render(request,"register.html",{"form":form})

    