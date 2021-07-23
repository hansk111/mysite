from django.db import models

# Create your models here.

class Sales(models.Model):
    year = models.IntegerField(default=0)
    sales = models.FloatField(default=0)
    before6_sales = models.FloatField(default=0)
    after6_sales = models.FloatField(default=0)
    machines = models.IntegerField(default=0)
    stocks = models.FloatField(default=0.0)
    korea_free_material = models.FloatField(default=0.0)
    global_free_material = models.FloatField(default=0.0)
    free_retrofit = models.FloatField(default=0.0)

class Amsales(models.Model):
    year = models.IntegerField(default=0)
    sales_plan = models.FloatField(default=0)
    sales = models.FloatField(default=0)
    
   


class Material(models.Model):
    year = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    korea_value = models.FloatField(default=0.0)
    china_value = models.FloatField(default=0.0)
    global_value = models.FloatField(default=0.0)
    goal_value = models.FloatField(default=0.0)
    sales_month_plan = models.FloatField(default=0.0)
    sales_month = models.FloatField(default=0.0)
    am_sales_month_plan = models.FloatField(default=0.0)
    am_sales_month = models.FloatField(default=0.0)
    