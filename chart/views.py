from django.shortcuts import render, redirect, resolve_url
from .models import Sales, Material, Amsales
# Create your views here.

def chart(request):
    sales = Sales.objects.all()
    amsales = Amsales.objects.all()
    free_of_charge = []
    for sale in sales:
        free_of_charge.append(sale.korea_free_material + sale.global_free_material + sale.free_retrofit)
   
    ye = request.POST.get('ye', '')
    if ye == '2020':
        material = Material.objects.all().filter(year=2020).order_by('month')
        
    elif ye == '2021':
        material = Material.objects.all().filter(year=2021).order_by('month')
        
    else:
        material = Material.objects.all()
        
    

    ye2 = request.POST.get('ye2', '')
    if ye2 == '2020':
        material2 = Material.objects.all().filter(year=2020).order_by('month')
        
    elif ye2 == '2021':
        material2 = Material.objects.all().filter(year=2021).order_by('month')
       
    else:
        material2 = Material.objects.all()
     
    

    context = {'sales': sales, 'amsales': amsales, 'material': material, 'material2': material2, 'ye': ye, 'ye2': ye2, 'free_of_charge' : free_of_charge }
   
    return render(request, 'chart/chart.html', context)