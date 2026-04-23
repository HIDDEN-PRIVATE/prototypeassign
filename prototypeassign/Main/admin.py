from django.contrib import admin
from .models import Course, ScalingGroup, UnitGroup, UnitGoals, ContentGroup, Assements
# Register your models here.
class UnitAdmin(admin.ModelAdmin):
    list_display = ["UnitName" , "Course"]

class AssementAdmin(admin.ModelAdmin):
    list_display = ["AssementName", "Unit", "Weighting", "StartDate", "EndDate"]

admin.site.register(Course)
admin.site.register(ScalingGroup)
admin.site.register(UnitGroup, UnitAdmin)
admin.site.register(UnitGoals)
admin.site.register(ContentGroup)
admin.site.register(Assements, AssementAdmin)

