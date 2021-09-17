from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
   return HttpResponse("index");

def hello(request):
   return render(request, "greet/hello.html")