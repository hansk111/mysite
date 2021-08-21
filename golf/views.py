from django.shortcuts import render, redirect, resolve_url
from .models import Fieldscore
from django.contrib.auth.decorators import login_required
import statistics
# Create your views here.


def screengolf(request):
    
    ye = request.POST.get('ye', '')
    if ye == '2018':
        fieldscore = Fieldscore.objects.all().filter(year=2018).order_by('date')
                
    elif ye == '2019':
        fieldscore = Fieldscore.objects.all().filter(year=2019).order_by('date')

    elif ye == '2020':
        fieldscore = Fieldscore.objects.all().filter(year=2020).order_by('date')
        
    elif ye == '2021':
        fieldscore = Fieldscore.objects.all().filter(year=2021).order_by('date')

    else:
        fieldscore = Fieldscore.objects.all()
    

    fscore = []
    for score in fieldscore:
        fscore.append(score.score)


    maxvalue = max(fscore)
    minvalue = min(fscore)
    averagevalue = statistics.mean(fscore)
    averagevalue = round(averagevalue, 1)

    context = {'fieldscore': fieldscore, 'ye': ye, 'maxvalue': maxvalue, 'minvalue': minvalue, 'averagevalue': averagevalue}

    return render(request, 'golf/screengolf.html', context)

def golfrule(request):
    return render(request, 'golf/golfrule.html')

def map(request):
    return render(request, 'golf/map.html')