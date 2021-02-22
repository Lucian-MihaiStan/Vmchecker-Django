from django.contrib import admin
from .models import Univ, UnivInstance, Year, Subject, Homework

# Register your models here.

admin.site.register(Univ)
admin.site.register(UnivInstance)
admin.site.register(Year)
admin.site.register(Subject)
admin.site.register(Homework)
