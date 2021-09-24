from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

class NewTaskForm(forms.Form):
    task = forms.CharField(label="")

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "todolist/index.html", {
        "tasks" : request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            
            return HttpResponseRedirect(reverse("todolist:index"))
    return render(request, "todolist/add.html", {
        "form" : NewTaskForm()
    })