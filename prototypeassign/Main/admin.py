from django.contrib import admin
from .models import Course, ScalingGroup, UnitGroup, UnitGoals, ContentGroup, Assements
# Register your models here.
admin.site.register(Course)
admin.site.register(ScalingGroup)
admin.site.register(UnitGroup)
admin.site.register(UnitGoals)
admin.site.register(ContentGroup)
admin.site.register(Assements)

