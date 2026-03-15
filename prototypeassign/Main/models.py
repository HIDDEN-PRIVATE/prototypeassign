from django.db import models

# Create your models here.


class UnitGroup(models.Model):
    #master Unit Group Name
    UnitName = models.CharField(max_length=25)
    #Course name
    Course = models.CharField(max_length=25)
    #Scaling Group
    ScalingGroup = models.CharField(max_length=25)
    #are year elevens Enrolled
    YearEleven = models.BooleanField()
    #are students from Year eleven markbook
    YearElvMarkbook = models.BooleanField()
    #are year twelves enrolled
    YearTwelve = models.BooleanField()
    #are students from Year twelve Markbook
    YearTweMarkbook = models.BooleanField()