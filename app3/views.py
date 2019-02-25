from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from .models import Person,Task
import json
# Create your views here.

class IndexView(ListView):
    template_name='app3/MemberManagement.html'

    def get_queryset(self):
        return Person.objects.all()

class TaskGenerationView(TemplateView):
    template_name='app3/Taskgeneration.html'

def tasksave(request):
    if request.method == 'POST':
        #for item in request.POST:
        #print(request.POST['Taskarea'])
        #res=TestingSlideAdd(request.POST['Duress1'],request.POST['Duress2'],request.POST['Duress3'],request.POST['Duress4'])
        task_instance = Task.objects.create(notes=request.POST['Tasknotes'],taskpolygon=request.POST['Taskarea'])

        context={'title':"This is the result of tasksave",
        'Taskarea':"here in py",
        'flag':'success'}
        return HttpResponse(json.dumps(context)) # if everything is OK
    # nothing went well
    return HttpResponse('FAIL!!!!!')
