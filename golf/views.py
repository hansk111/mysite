from django.shortcuts import render

# Create your views here.

def screengolf(request):
    return render(request, 'golf/screengolf.html')

def golfrule(request):
    return render(request, 'golf/golfrule.html')