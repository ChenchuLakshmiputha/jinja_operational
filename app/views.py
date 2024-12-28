from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'name':'lakshmi','age':22,'a':100}
    return render(request,'conditions.html',d)