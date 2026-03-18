from tkinter import CASCADE
from django.db import models

# Create your models here.
class Course(models.Model):
    Coursename = models.CharField(max_length=25)

class ScalingGroup(models.Model):
    ScalinggroupName = models.CharField(max_length=25)

class UnitGroup(models.Model):
    #master Unit Group Name
    UnitName = models.CharField(max_length=25)
    #Course name
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    #Scaling Group
    ScalingGroup = models.ForeignKey(ScalingGroup, on_delete=models.CASCADE)
    #are year elevens Enrolled
    YearEleven = models.BooleanField()
    #are students from Year eleven markbook
    YearElvMarkbook = models.BooleanField()
    #are year twelves enrolled
    YearTwelve = models.BooleanField()
    #are students from Year twelve Markbook
    YearTweMarkbook = models.BooleanField()

class Assements(models.Model):
    AssementName = models.CharField(max_length=10)
    Weighting = models.PositiveIntegerField()
    StartDate = models.DateField()
    EndDate = models.DateField()
    Unit = models.ForeignKey(UnitGroup, on_delete=models.CASCADE)


class ContentGroup(models.Model):
    ContentName = models.CharField(max_length=10)
    Unit = models.ForeignKey(UnitGroup, on_delete=models.CASCADE)

class UnitGoals(models.Model):
    GoalName = models.CharField(max_length=50)
    GoalDescription = models.CharField()
    Unit = models.ForeignKey(UnitGroup, on_delete=models.CASCADE)
