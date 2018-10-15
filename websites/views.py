from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView
from .models import Site
# Create your views here.
def welcome(request):
    context = {
        'sites': Site.objects.all()
    }
    return render(request,'websites/tech_home.html', context)
class SiteListView(ListView):
    model = Site
    template_name = 'websites/tech_home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'sites'
    ordering = ['-date_posted']

class SiteDetailView(DetailView):
    model = Site

class SiteCreateView(CreateView):
    model = Site
    fields = ['title','image','description','site_url']
