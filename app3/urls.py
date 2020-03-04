from django.urls import path
from django.views.generic import TemplateView
from . import views
from app3.views import IndexView,TaskGenerationView,TaskGenerationFormView,TaskassignmentExperimentView,TaskassignmentFullView
from django.conf.urls import url
from rest_framework import routers
from django.conf.urls import include

router = routers.DefaultRouter()
router.register(r'gpsdatas', views.GPSDataViewSet,basename="gpsdatas")

urlpatterns = [
    path('', TaskGenerationView.as_view(),name='mapdivisioninit'),
    path('experiment', TaskassignmentExperimentView.as_view(),name='experiment'),
    path('full', TaskassignmentFullView.as_view(),name='full'),
    path('members', IndexView.as_view()),
    path('edit',TemplateView.as_view(template_name="app3/edit.html"),name='edit'),
    path('sketch',TemplateView.as_view(template_name="app3/sketch.html")),
    path('formdemo',TemplateView.as_view(template_name="app3/FormDemo.html")),
    path('taskgenerationform',TaskGenerationFormView.as_view(),name="taskgenerationform"),
    path('action_page', TaskGenerationFormView.FormToDB),#.get_values
    path('offlinemapdemo',TemplateView.as_view(template_name="app3/offlinemapdemo.html")),
    url(r'^tasksave$',TaskGenerationView.tasksave,name='tasksave'),
    url(r'^gpsupdate$',TaskGenerationView.gpsupdate,name='gpsupdate'),
    url(r'^getwatershed$',TaskGenerationView.getwatershed,name='getwatershed'),
    url(r'^gpsdatastorage$',TaskGenerationView.gpsdatastorage,name='gpsdatastorage'),
    url(r'^demo$',TemplateView.as_view(template_name="app3/demo.html"), name="demo"),
    url(r'^openstreatmap$',TemplateView.as_view(template_name="app3/openstreatmap.html"), name="openstreatmap"),
    url(r'^taskgenerationform/(?P<task_id>\w+)_(?P<subtask_id>\d+)/$',TaskGenerationFormView.as_view(),name="taskgenerationform"),
    url(r'^taskgenerationform/\w+/action_page$',TaskGenerationFormView.FormToDB,name="action_page"),
    url(r'^readfile$',TemplateView.as_view(template_name="app3/readfile.html"), name="readfile"),
    path('api-auth/', include('rest_framework.urls')),
    path('layerquerytest',TemplateView.as_view(template_name="app3/layerquerytest.html")),
    path('watershed',TemplateView.as_view(template_name="app3/watershed.html"),name='watershed'),
    path('heatmapringdownload',TemplateView.as_view(template_name="app3/Taskgeneration_download.html")),
    path('videostream',TemplateView.as_view(template_name="app3/UAVVideostream.html")),
    path('index',TemplateView.as_view(template_name="app3/index.html")),
]

urlpatterns += router.urls
#print(urlpatterns)
