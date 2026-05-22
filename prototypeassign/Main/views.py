#imports Render which is vital and Get_object_or_404 which gets a single item, or a 404 https response, instead of error
import re
from urllib import response
from django.shortcuts import redirect, render
from django.shortcuts import render, get_object_or_404 #might be able to remove render from here and 404 up
from django.template import Context, Template, context
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from pypdf import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Image, Table
from django.http import FileResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from io import BytesIO

# imports models and forms from main
from .models import Course, ScalingGroup, UnitGroup, Assements, ContentGroup, UnitGoals
from .forms import InputForm

#Authenciation for user accounts
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages #perhaps remove
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

def PdfGener():
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    lines = ['Assement name:', 'Weight', 'start Date:', 'End Date:', 'Unit', 'Group:', 'Goal:', 'Description:']

    assemen = Assements.objects.all()
    groups = ContentGroup.objects.all()
    Goals = UnitGoals.objects.all()


    for Assmenent in assemen:
        lines.append((Assmenent.AssementName, Assmenent.Weighting, Assmenent.StartDate, Assmenent.EndDate, Assmenent.Unit))
    
    for group in groups:
        lines.append((group.ContentName))
    for goal in Goals:
        lines.append((goal.GoalName, goal.GoalDescription))
    
    table = Table(lines)
    table.wrapOn(p, 0, 0)
    table.drawOn(p, 0, 450)
    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer

def report(request):

    pdf_file =  staticfiles_storage.path("EON15P-1_1_.pdf")

    try:
        merger = PdfWriter()

        input1 = PdfReader(PdfGener())
        input2 = PdfReader(pdf_file, "rb")

        merger.append(input1)
        merger.append(input2)

        buffer = BytesIO()
        merger.write(buffer)
        buffer.seek(0)

        response = FileResponse(buffer, as_attachment=True, filename="report.pdf")


    except FileNotFoundError:
        response = FileResponse(PdfGener(), as_attachment=True, filename='no.pdf')

    return response

    



# Create your views here.

def index(request): #Home
    
    MasterUnit = UnitGroup.objects.all()
    return render(request,"Main/index.html", {'content': MasterUnit}) #should replace with Context at some point

@login_required(login_url='/login')

def outline(request, id): #unit outline Generator Template
    

    UnitName = get_object_or_404(UnitGroup, id=id)
    UnitAssement = Assements.objects.filter(Unit=UnitName)
    Content = ContentGroup.objects.filter(Unit=UnitName)
    goals = UnitGoals.objects.filter(Unit=UnitName)
    #allows creation of new assignments
    if request.user.groups.filter(name="test").exists():
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
    else:
        return redirect(index)

def assigndel(request, id):
    Assem = get_object_or_404(Assements, id=id)
    Assem.delete()
    return redirect(request.META.get('HTTP_REFERER'))
#

#login view will be here
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"] 
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(index)
        else:
            messages.error(request, 'Invalid username or password.')
            
    form = AuthenticationForm()
    return render(request,"Main/login.html", {'form':form, 'title':'log in'})

def logout_view(request):
    logout(request)
    return redirect(index)