from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    
    return render(request,"index.html")


def homepage(request):
    return render(request,"homepage.html")

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request,"homepage.html",{"user":user})
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect("/")



def register_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        user = form.save()
        login(request, user)
        return render(request,"index.html")
    else:
        form = UserCreationForm()

    return render(request,"register.html",{"form":form})




