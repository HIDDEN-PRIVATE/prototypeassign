from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.template import Context, Template, context
from .models import Course, ScalingGroup, UnitGroup, Assements, ContentGroup, UnitGoals

# Create your views here.

def index(request):
    
    MasterUnit = UnitGroup.objects.all()
    return render(request,"Main/index.html", {'content': MasterUnit})
def outline(request, id):
     
    UnitName = get_object_or_404(UnitGroup, id=id)
    UnitAssement = Assements.objects.filter(Unit=UnitName)
    Content = ContentGroup.objects.filter(Unit=UnitName)
    goals = UnitGoals.objects.filter(Unit=UnitName)
    context = {
        "UnitName": UnitName,
        "UContent": Content,
        "Assement":UnitAssement,
        "Ugoals":goals
        }
    return render(request, "Main/outlinetemplate.html", context)