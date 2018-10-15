from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
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

class SiteCreateView(LoginRequiredMixin, CreateView):
    model = Site
    fields = ['title','image','description','site_url']

    def form_valid(self, form):
        form.instance.developer = self.request.user
        return super().form_valid(form)
