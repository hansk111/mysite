from django.contrib import admin
from .models import Fieldscore

# Register your models here.

class FieldscoreAdmin(admin.ModelAdmin):
    list_display = ['club','year','date', 'score', 'companion1','companion2','companion3',]


admin.site.register(Fieldscore, FieldscoreAdmin)

