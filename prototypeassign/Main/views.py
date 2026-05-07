#imports Render which is vital and Get_object_or_404 which gets a single item, or a 404 https response, instead of error
import re
from django.shortcuts import redirect, render
from django.shortcuts import render, get_object_or_404 #might be able to remove render from here and 404 up
from django.template import Context, Template, context

# imports models and forms from main
from .models import Course, ScalingGroup, UnitGroup, Assements, ContentGroup, UnitGoals
from .forms import InputForm

#Authenciation for user accounts
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages #perhaps remove

# Create your views here.

def index(request): #Home
    
    MasterUnit = UnitGroup.objects.all()
    return render(request,"Main/index.html", {'content': MasterUnit}) #should replace with Context at some point


def outline(request, id): #unit outline Generator Template
    if not User.is_authenticated:
        return redirect('home')

    UnitName = get_object_or_404(UnitGroup, id=id)
    UnitAssement = Assements.objects.filter(Unit=UnitName)
    Content = ContentGroup.objects.filter(Unit=UnitName)
    goals = UnitGoals.objects.filter(Unit=UnitName)

    #allows creation of new assignments
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            Assem = form.save(commit = False)
            Assem.Unit = UnitName
            Assem.save()

    else:
        form = InputForm()
    #allows for importing of multiple Models
    context = {
        "UnitName": UnitName,
        "UContent": Content,
        "Assement":UnitAssement,
        "Ugoals":goals,
        "form": form
        }
    return render(request, "Main/outlinetemplate.html", context)

def assigndel(request, id):
    Assem = get_object_or_404(Assements, id=id)
    Assem.delete()
    return redirect(request.META.get('HTTP_REFERER'))

#login view will be here