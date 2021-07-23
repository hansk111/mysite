from django.contrib import admin
from .models import Sales, Material, Amsales

# Register your models here.

class SalesAdmin(admin.ModelAdmin):
    list_display = ['year','sales','before6_sales', 'after6_sales', 'machines','stocks','korea_free_material','global_free_material','free_retrofit']

class AmsalesAdmin(admin.ModelAdmin):
    list_display = ['year','sales_plan','sales']


class MateralAdmin(admin.ModelAdmin):
    list_display = ['year','month','korea_value','china_value','global_value','goal_value', 'sales_month_plan', 'sales_month','am_sales_month_plan','am_sales_month']

admin.site.register(Sales, SalesAdmin)
admin.site.register(Material, MateralAdmin)
admin.site.register(Amsales, AmsalesAdmin)