from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'learning/home.html')
    
def contacts(request):
    return render(request, 'learning/contact.html')
def about(request):
    return render(request, 'learning/about.html')