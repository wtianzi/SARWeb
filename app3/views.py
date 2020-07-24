from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView
from django.http import HttpResponse,HttpResponseRedirect
from .models import Person,Task,GPSData,DataStorage,ClueMedia
import json
from .forms import DemoForm,TaskAssignmentForm
from django.urls import reverse
from django.template import loader
from django.core import serializers
from rest_framework import viewsets
from .serializers import GPSDataSerializer,ClueMediaSerializer

from rest_framework import permissions

from .py.watershed import AreaSegment
from .py.contourmapanalysis import SegmentWeight
# Create your views here.


class IndexView(ListView):
    template_name='app3/MemberManagement.html'

    def get_queryset(self):
        return Person.objects.all()

class TaskGenerationView(TemplateView):
    template_name='app3/Taskgeneration.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        #tasks_all=Task.objects.only('taskid').distinct('taskid')
        tasks_all=list(Task.objects.exclude(taskid=None).values_list('taskid', flat=True).distinct())
        #print(tasks_all)
        context['task_all']=tasks_all
        last_n_deviceid=GPSData.objects.values().order_by('-updated_at')[:5]
        context['gpsdevice']=last_n_deviceid
        return context

    def get_values(request):
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = DemoForm(request.POST)
            #print(form)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                # form.save_to_db()
                return render(request, 'app3/demo.html', {'form': form})#HttpResponseRedirect('sketch')

        # if a GET (or any other method) we'll create a blank form
            else:
                form = DemoForm()
            return render(request, 'app3/demo.html', {'form': form})

    def tasksave(request):
        if request.method == 'POST':
            #for item in request.POST:
            #print(request.POST['Taskarea'])
            #res=TestingSlideAdd(request.POST['Duress1'],request.POST['Duress2'],request.POST['Duress3'],request.POST['Duress4'])
            task_instance = Task.objects.create(notes=request.POST['task_notes'],taskid=request.POST['task_id'],taskpolygon=request.POST['task_polygon'])

            context={'title':"This is the result of tasksave",
            'Taskarea':"here in py",
            'flag':'success'}
            return HttpResponse(json.dumps(context)) # if everything is OK
        # nothing went well
        return HttpResponse('FAIL!!!!!')

    def gpsupdate(request):
        if request.method == 'POST':
            gpsdata_id = request.POST['id_device_id']
            gpsitem = GPSData.objects.get(deviceid=gpsdata_id)
            context={'gpsdata':getattr(gpsitem, 'gpsdata'),'flag':'success'}
            #print(context)
            return HttpResponse(json.dumps(context)) # if everything is OK
        # nothing went well
        return HttpResponse('FAIL!!!!!')

    def gpsdatastorage(request):
        if request.method == 'POST':
            t_datastorage=DataStorage()
            t_datastorage.taskid = request.POST['task_notes']
            t_datastorage.subtaskid = request.POST['id_device_id']+"_"+request.POST['rand_gpsdevicename']

            all_gpsdata=request.POST.get('all_gpsdata')
            #print(all_gpsdata)

            t_datastorage.data = {'device_id':request.POST['device_id'],'gps':all_gpsdata}
            t_datastorage.save()
            context={'gpsdata':all_gpsdata,'flag':'success'}

            return HttpResponse(json.dumps(context)) # if everything is OK
        # nothing went well
        return HttpResponse('FAIL!!!!!')

    def getwatershed(request):
        if request.method == 'POST':
            elevation_arr = request.POST.get('elevation_arr')
            img_w=request.POST['width']
            img_h=request.POST['height']

            #image processing watershed opencv pyhon
            tjson=json.loads(elevation_arr)
            #print(tjson)
            res=AreaSegment.GetWatershedPolygon_contours(tjson,int(img_w),int(img_h),1)
            #res=AreaSegment.GetWatershedPolygon_vironoi(tjson,int(img_w),int(img_h),1)
            #res=AreaSegment.GetAdaptiveThresholdingPolygon(tjson,int(img_w),int(img_h),1)

            context={'watershedpolygon':res,'flag':'success'}
            #print(context)

            return HttpResponse(json.dumps(context)) # if everything is OK
        # nothing went well
        return HttpResponse('Getwatershed failed!')

    def getClueMedia(request):
        if request.method == 'POST':
            clue_id = request.POST['photoid']
            clueitem = ClueMedia.objects.get(id=int(clue_id))

            context={'cluephotoid':str(clueitem.id),
                    'name':str(clueitem.name),
                    'lon':str(clueitem.longitude),
                    'lat':str(clueitem.latitude),
                    'url':str(clueitem.photo.url),
                    'detail':str(clueitem.description),
                    'flag':'success'}
            #print(context)
            return HttpResponse(json.dumps(context)) # if everything is OK
        # nothing went well
        return HttpResponse('FAIL!!!!!')

    def getSegmentVal(request):
        if request.method == 'POST':
            print("getSegmentVal")
            contourarr = request.POST.get('contourarr')
            voronoiarr = request.POST.get('voronoiarr')
            spatialReference = request.POST.get('spatialReference')
            #image processing segment opencv pyhon
            contourjson=json.loads(contourarr)
            voronoijson=json.loads(voronoiarr)
            #print(tjson)
            res,arr_vor=SegmentWeight(contourjson,voronoijson,spatialReference)

            context={'segmentval':res,'updatevoronoi':arr_vor,'flag':'success'}
            #print(context)

            return HttpResponse(json.dumps(context)) # if everything is OK
        # nothing went well
        return HttpResponse('Getwatershed failed!')



class TaskIndexView(TemplateView):
    template_name="app3/index.html"
    #def get_queryset(self):
    def get(self, request, *args, **kwargs):
        img=ClueMedia.objects.all()
        context ={'message': img}
        return render(request, 'app3/index.html',context=context)
    def get_context_data(self, *args, **kwargs):
        context = super(Home. self).get_context_data(*args, **kwargs)
        context['message'] = 'Hello World!'
        return context
        #return  render_to_response("app3/index.html", {"img": img})

class TaskGenerationFormView(TemplateView):
    template_name="app3/taskgenerationform.html"
    #polygongs=Task.objects.get(id=14)
    #number of areas,

    #{'0':{'form':{'task_instructions':'[][][][]','task_complete':'yes'} ,'buttonmuber':20 },'1':{} }
    context={"form":{"task_instractions":"polygongs"}}#{'task_instructions': "[[1,1],[2,2]]"}

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        #polygons=Task.objects.get(taskid=kwargs['task_id'])
        polygons=Task.objects.filter(taskid=kwargs['task_id']).latest('id')
        if (polygons is not None):
            context["task_id"] = kwargs['task_id']
            if(len(polygons.taskpolygon)>10):
                taskpolygon_json=json.loads(polygons.taskpolygon)
                subtaskpolygon=taskpolygon_json[kwargs['subtask_id']]
                plytsr=str(subtaskpolygon).replace('[','').replace('],',';\r').replace(']','').replace(' ','')
                context["form"] = {"task_instractions":plytsr,"task_number":kwargs['task_id']}#self.context["form"]
                context["subtask_id"] = int(kwargs['subtask_id'])
                context["subtask_sum"] = range(len(taskpolygon_json))
            else:
                context["form"] = {"task_instractions":"Please generate searching areas for the task in the previous page!","task_number":kwargs['task_id']}
                context["subtask_id"] = 1
                context["subtask_sum"] = [1]
        return context

    def FormToDB(request):
        form=TaskAssignmentForm(request.POST or None)
        #print(request.POST)
        if form.is_valid():
            form.save()
        context={'form': form}
        #print(form)
        return render(request,'app3/demo.html',context)


class GPSDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.

    import requests
    r = requests.get('http://127.0.0.1:8000/gpsdatas/')
    r = requests.patch('http://127.0.0.1:8000/app3/gpsdatas/max_testing/', auth=('username','password'), data = {'deviceid':'max_testing', 'taskid':'sar_put2','gpsdata':'{"gps":["stamp":004,"lat":-80,"log":38]}'})
    r = requests.post('http://127.0.0.1:8000/app3/gpsdatas/', auth=('username','password'),data = {'deviceid':'max_test_100', 'taskid':'sar_put2','gpsdata':'{"gps":["stamp":004,"lat":-80,"log":38]}'})
    r.text

    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = GPSData.objects.all()
    serializer_class = GPSDataSerializer

class ClueMediaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.

    import base64
    import requests

    # filnename is the location of where the image are sent from
    filename="D:/Projects/SARWeb/static/img/cluesamples/thermal_sample.png"

    # url are the target IP address and port + "/cluemedia/", for example, http://172.29.20.199:8000/cluemedia/
    url = "http://127.0.0.1:8000/cluemedia/"

    # the format of uploading files
    # files = {'photo': open(filename, 'rb')}

    # requests.get is to view the existing data
    r = requests.get(url)

    # requests.post is to create a new item in the database
    r = requests.post(url,
        auth=(username,password),
        data = {'id':'2', 'name':'Drone2','longitude':'-80.543407', 'latitude':'37.196209', 'description':'Thermal camera top view'},
        files={'photo':open(filename, 'rb')}
        )
    # requests.patch is to update an existing item in the database, the url need to add a index
    r=requests.patch('http://127.0.0.1:8000/cluemedia/2/',
        auth=(username,password),
        data = {'id':'2', 'name':'Drone2','longitude':'-80.543407', 'latitude':'37.196209', 'description':'Thermal camera top view'},
        files={'photo':open(filename, 'rb')}
        )
    print (r.text)
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = ClueMedia.objects.all()
    serializer_class = ClueMediaSerializer

class TaskassignmentExperimentView(TemplateView):
    #template_name='app3/Taskgeneration_exp.html'
    template_name='app3/Taskgeneration_exp_v1.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        #tasks_all=Task.objects.only('taskid').distinct('taskid')
        tasks_all=list(Task.objects.exclude(taskid=None).values_list('taskid', flat=True).distinct())
        #print(tasks_all)
        context['task_all']=tasks_all#["SAR0001"]#tasks_all

        #json_serializer = serializers.get_serializer("json")()
        #gpsdata = json_serializer.serialize(GPSData.objects.all().order_by('id')[:5], ensure_ascii=False)
        #tempstr=GPSData.objects.values_list('gpsdata', flat=True).get(pk=1)

        #list the last 5 device and let the user to select which one to mark gps
        #last_n_deviceid=GPSData.objects.values_list('deviceid').order_by('-id')[:5]
        last_n_deviceid=GPSData.objects.values().order_by('-updated_at')[:5]
        #print(last_n_deviceid)
        context['gpsdevice']=last_n_deviceid
        #gpsdata_all=list(GPSData.objects.all().values_list('deviceid', flat=True).distinct())

        #for testing, get gps data from id=3
        #test = GPSData.objects.get(id=3)
        #test.refresh_from_db()
        #context['gpsdata']=getattr(test, 'gpsdata')

        return context

    def get_values(request):
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = DemoForm(request.POST)
            #print(form)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                #form.save_to_db()
                return render(request, 'app3/demo.html', {'form': form})#HttpResponseRedirect('sketch')

        # if a GET (or any other method) we'll create a blank form
            else:
                form = DemoForm()
            return render(request, 'app3/demo.html', {'form': form})

    def tasksave(request):
        if request.method == 'POST':
            #for item in request.POST:
            #print(request.POST['Taskarea'])
            #res=TestingSlideAdd(request.POST['Duress1'],request.POST['Duress2'],request.POST['Duress3'],request.POST['Duress4'])
            task_instance = Task.objects.create(notes=request.POST['task_notes'],taskid=request.POST['task_id'],taskpolygon=request.POST['task_polygon'])

            context={'title':"This is the result of tasksave",
            'Taskarea':"here in py",
            'flag':'success'}
            return HttpResponse(json.dumps(context)) # if everything is OK
        # nothing went well
        return HttpResponse('FAIL!!!!!')

    def gpsupdate(request):
        if request.method == 'POST':
            gpsdata_id = request.POST['id_device_id']
            gpsitem = GPSData.objects.get(id=gpsdata_id)
            context={'gpsdata':getattr(gpsitem, 'gpsdata'),'flag':'success'}
            return HttpResponse(json.dumps(context)) # if everything is OK
        # nothing went well
        return HttpResponse('FAIL!!!!!')

    def gpsdatastorage(request):
        if request.method == 'POST':
            t_datastorage=DataStorage()
            t_datastorage.taskid = request.POST['task_notes']
            t_datastorage.subtaskid = request.POST['id_device_id']+request.POST['rand_gpsdevicename']

            all_gpsdata=request.POST.get('all_gpsdata')

            t_datastorage.data = {'device_id':request.POST['device_id'],'gps':all_gpsdata}
            t_datastorage.save()
            context={'gpsdata':all_gpsdata,'flag':'success'}

            return HttpResponse(json.dumps(context)) # if everything is OK
        # nothing went well
        return HttpResponse('FAIL!!!!!')

    def getwatershed(request):
        if request.method == 'POST':
            elevation_arr = request.POST.get('elevation_arr')
            img_w=request.POST['width']
            img_h=request.POST['height']

            #image processing watershed opencv pyhon
            tjson=json.loads(elevation_arr)
            #print(tjson)
            res=AreaSegment.GetWatershedPolygon_contours(tjson,int(img_w),int(img_h),1)
            #res=AreaSegment.GetWatershedPolygon_vironoi(tjson,int(img_w),int(img_h),1)
            #res=AreaSegment.GetAdaptiveThresholdingPolygon(tjson,int(img_w),int(img_h),1)

            context={'watershedpolygon':res,'flag':'success'}
            #print(context)

            return HttpResponse(json.dumps(context)) # if everything is OK
        # nothing went well
        return HttpResponse('Getwatershed failed!')

class TaskassignmentFullView(TaskassignmentExperimentView):
    template_name='app3/Taskgeneration_full.html'
