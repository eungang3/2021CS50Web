import time
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, "post/index.html")

def posts(request):
    