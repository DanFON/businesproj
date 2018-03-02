
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# create your views here.
def home(request):
    context = {}
    templates = 'home.html'
    return render(request, templates, context)

def support_services(request):
    context = {}
    templates = 'support_services.html'
    return render(request, templates, context)

def maintenance(request):
    context = {}
    templates = 'maintenance.html'
    return render(request, templates, context)