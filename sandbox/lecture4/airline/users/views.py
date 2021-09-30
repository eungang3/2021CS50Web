from django.shortcuts import render
from django.urls import reverse 
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    # If no user is signed in, return to login page:
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user :
            login(request, user)
            return HttpResponseRedirect((reverse("index")))
        else:
            return render(request, "users/login.html", {
                "message" : "Invalid Credentials"
            })
    return render(request, "users/login.html")

def logout_view(request):
    # Pass is a simple way to tell python to do nothing.
    logout(request)
    return render(request, "users/login.html", {
        "message":"Logged out"
    })