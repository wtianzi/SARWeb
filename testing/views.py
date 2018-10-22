from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from testing.ml import multiply,TestingSlideAdd
import json

def index(request):

    res=[1,2,3,4]

    template = loader.get_template('testing/jspy.html')

    context={'title':"Hello, welcome to our lab. Testing page for app 1.",
    'DuressJ1':res[0],
    'DuressJ2':res[1],
    'DuressJ3':res[2],
    'DuressJ4':res[3]}
    return HttpResponse(template.render(context,request))

def DuressTesting(request):
    if request.method == 'POST':
        #for item in request.POST:
        res=multiply(request.POST['Duress1'],request.POST['Duress2'],request.POST['Duress3'],request.POST['Duress4'])
        context={'title':"This is the result of Duresstesting",
        'DuressJ1':res[0],
        'DuressJ2':res[1],
        'DuressJ3':res[2],
        'DuressJ4':res[3],
        'flag':'success'}
        return HttpResponse(json.dumps(context)) # if everything is OK
    # nothing went well
    return HttpResponse('FAIL!!!!!')

def DuressTestingAdd(request):
    if request.method == 'POST':
        #for item in request.POST:
        res=TestingSlideAdd(request.POST['Duress1'],request.POST['Duress2'],request.POST['Duress3'],request.POST['Duress4'])
        
        context={'title':"This is the result of DuresstestingAdd",
        'DuressJ1':res[0],
        'DuressJ2':res[1],
        'DuressJ3':res[2],
        'DuressJ4':res[3],
        'flag':'success'}
        return HttpResponse(json.dumps(context)) # if everything is OK
    # nothing went well
    return HttpResponse('FAIL!!!!!')
