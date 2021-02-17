from django.contrib import admin
from .models import Univ, UnivInstance, Year, YearInstance, Subject, SubjectInstance, Homework, HomeworkInstance

# Register your models here.

admin.site.register(Univ)
admin.site.register(UnivInstance)
admin.site.register(Year)
admin.site.register(YearInstance)
admin.site.register(Subject)
admin.site.register(SubjectInstance)
admin.site.register(Homework)
admin.site.register(HomeworkInstance)
