from django.shortcuts import render
from django.views import View, generic


# Create your views here.
class Index(generic.TemplateView):
    template_name = 'task_management/index.html'