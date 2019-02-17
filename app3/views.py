from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from .models import Person
# Create your views here.

class IndexView(ListView):
    template_name='app3/MemberManagement.html'

    def get_queryset(self):
        return Person.objects.all()

class TaskGenerationView(TemplateView):
    template_name='app3/Taskgeneration.html'
