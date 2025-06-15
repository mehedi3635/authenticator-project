from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def regestation(request):
    return render(request, 'regestation.html')
def loging(request):
    return render(request, 'loging.html')