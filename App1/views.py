from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('App1/index.html')
    context={'title':"Hello, welcome to our lab. Testing page for app 1."}
    return HttpResponse(template.render(context,request))
    
# Create your views here.
