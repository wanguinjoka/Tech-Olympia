from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request,'websites/tech_home.html')
