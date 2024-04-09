from django.shortcuts import render,redirect
from django.utils.translation import gettext_lazy as _,activate
from . import forms

# Create your views here.
def home_(r):
    return render(r,"home.html")
def Contect(r):
    return render(r,"contect.html")
def about(r):
    return render(r,"about.html")
def changeLanguage(r):
    if r.method=="POST":
        language=r.POST["language"]
        activate(language)
        return redirect("homePage")
    return render(r,"changeLanguage.html")