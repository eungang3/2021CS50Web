from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
import markdown2
from . import util

class NewEntryForm(forms.Form):
    title = forms.CharField(label="title", widget=forms.TextInput(attrs={'placeholder': 'Enter title', 'style':'width:30%; margin-bottom: 1rem;'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter contents', 'style':'width:80%; height:500px; margin-bottom: 1rem;'}), label="content")


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def create(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            # check if the entry already exists
            entries = util.list_entries()
            for entry in entries:
                if entry.lower() == title.lower():
                    return render(request, "encyclopedia/error.html", {
                        "message" : "Entry already Exists. Try editing the existing entry."
                    })
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("encyclopedia:index"))
    else:
        return render(request, "encyclopedia/create.html", {
            "form" : NewEntryForm()
         })

def entry(request, title):
    entry = util.get_entry(title)
    if not entry:
        return render(request, "encyclopedia/error.html", {
            "message" : "Entry does not exist."
        })
    html_entry = markdown2.markdown(entry)
    return render(request, "encyclopedia/entry.html", {
        "title" : title,
        "entry" : html_entry
    })

def search(request):
    query = request.POST["q"].lower()
    entries = util.list_entries()
    matches = []
    for entry in entries:
        # if there's a perfect match, redirect to that entry
        if entry.lower() == query:
            return render(request, "encyclopedia/entry.html", {
                "title" : entry,
                "entry" : markdown2.markdown(util.get_entry(entry))
            })
        # check if query is entry's substring
        if query in entry.lower():
            matches.append(entry)
    # if there's no perfect match, show search result page        
    return render(request, "encyclopedia/search.html", {
        "query": query,
        "matches":matches
    })