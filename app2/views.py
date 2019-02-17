from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from app2.models import Person

def index(request):
    template = loader.get_template('app2/ArcGISTriangles.html')
    context={'title':"Hello, welcome to our lab. Testing page for app 2."}
    return HttpResponse(template.render(context,request))

def lattice(request):
    template = loader.get_template('app2/lattice.html')
    context={'title':"Hello, welcome to our lab. Testing page for app 2."}
    return HttpResponse(template.render(context,request))

def ShowAllMembers(request):
    Person.objects.all()
    template = loader.get_template('app2/MemberManagement.html')
    context={'title':"Hello, here are all the members."}
    return HttpResponse(template.render(context,request))

# Create your views here.

def graphs(request):
    template = loader.get_template('app2/graphs.html')
    context={'title':"Hello, welcome to our lab. Testing page for app 1."}
    return HttpResponse(template.render(context,request))

def blocks(request):
    template = loader.get_template('app2/blocks.html')
    context={'title':"Hello, welcome to our lab. Testing page for app 1."}
    return HttpResponse(template.render(context,request))

def dragpoints(request):
    template = loader.get_template('app2/dragpoints.html')
    context={'title':"Hello, welcome to our lab. Testing page for app 1."}
    return HttpResponse(template.render(context,request))

def lattice(request):
    template = loader.get_template('app2/lattice.html')
    context={'title':"Hello, welcome to our lab. Testing page for app 1."}
    return HttpResponse(template.render(context,request))

def voronoi(request):
    template = loader.get_template('app2/voronoi.html')
    context={'title':"Hello, welcome to our lab. Testing page for app 1."}
    return HttpResponse(template.render(context,request))

def multilinevoronoi(request):
    template = loader.get_template('app2/multilinevoronoi.html')
    context={'title':"Hello, welcome to our lab. Testing page for app 1."}
    return HttpResponse(template.render(context,request))

def circle(request):
    template = loader.get_template('app2/circle.html')
    context={'title':"Hello, welcome to our lab. Testing page for app 1."}
    return HttpResponse(template.render(context,request))

def d3v3voronoi(request):
    template = loader.get_template('app2/d3v3voronoi.html')
    context={'title':"Hello, welcome to our lab. Testing page for app 1."}
    return HttpResponse(template.render(context,request))

def arcgis(request):
    template = loader.get_template('app2/ArcGISAPI.html')
    context={'title':"Hello, welcome to our lab. Testing page for app 1."}
    return HttpResponse(template.render(context,request))

def arcgisc(request):
    template = loader.get_template('app2/ArcGISAPICircle.html')
    context={'title':"Hello, welcome to our lab. Testing page for app 1."}
    return HttpResponse(template.render(context,request))

def arcgisv(request):
    template = loader.get_template('app2/ArcGISVoronoi.html')
    context={'title':"Hello, welcome to our lab. Testing page for app 1."}
    return HttpResponse(template.render(context,request))
