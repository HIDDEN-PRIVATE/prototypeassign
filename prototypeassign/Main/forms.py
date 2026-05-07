from dataclasses import fields
from django import forms
from .models import Course, ScalingGroup, UnitGroup, Assements, ContentGroup, UnitGoals

class InputForm(forms.ModelForm):
    class Meta:
        model = Assements
        exclude = ['Unit']

        
    