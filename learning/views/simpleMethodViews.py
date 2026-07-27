from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'learning/home.html')
    
def contacts(request):
    return render(request, 'learning/contact.html')
def about(request):
    return render(request, 'learning/about.html')
def studentslist(request,**kwargs):
    st_number = kwargs.get('st_number')
    page_number = kwargs.get('page_number')
    if(page_number*10 > st_number):
        return render(request, 'learning/studentslist.html')
    return render(request, 'learning/studentslist.html',context={
        'students_number':range((page_number-1)*10,page_number*10),
        'students_number_count':10,
        'page_number':page_number,
        })
