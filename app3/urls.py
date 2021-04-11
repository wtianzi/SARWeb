from django.urls import path
from django.views.generic import TemplateView
from . import views
from app3.views import IndexView,TaskGenerationView,TaskGenerationFormView,TaskassignmentExperimentView,TaskassignmentFullView,TaskIndexView,QuestionnaireFormView,ConsentFormView,SurveyPostEFormView,DemogrphicsView, WebapplicationFormView
from app3.views import DownloadDataView
from django.conf.urls import url
from rest_framework import routers
from django.conf.urls import include

router = routers.DefaultRouter()
router.register(r'gpsdatas', views.GPSDataViewSet,basename="gpsdatas")
router.register(r'cluemedia', views.ClueMediaViewSet,basename="cluemedia")
router.register(r'waypointsdata', views.WaypointsDataViewSet,basename="waypointsdata")
router.register(r'gpshistoricaldata', views.GPShistoricalDataViewSet,basename="gpshistoricaldata")

urlpatterns = [
    path('', TaskGenerationView.as_view(),name='mapdivisioninit'),

    url(r'^experiment/task/$', TaskassignmentExperimentView.as_view(),name='experiment'),
    url(r'^experiment/task/(?P<participantid>\w+)/$',TaskassignmentExperimentView.as_view(),name="experiment"),
    url(r'^experiment/task/(?P<participantid>\w+)/(?P<participantindex>\w+)/$',TaskassignmentExperimentView.as_view(),name="experiment"),

    path('experiment/consentform',ConsentFormView.as_view(),name='consentform'),
    path('experiment/consentform_action', ConsentFormView.FormToDB),
    
    path('experiment/demos',DemogrphicsView.as_view(),name="demos"),
    url(r'^experiment/demos/(?P<participantid>\w+)/(?P<participantindex>\w+)/$',DemogrphicsView.as_view(),name="demos"),
    url(r'^experiment/demos/\w+/\w+/action$', DemogrphicsView.FormToDB,name="demos"),
        
    path('experiment/survey_postexperiment',SurveyPostEFormView.as_view(),name="survey_postexperiment"),
    url(r'^experiment/survey_postexperiment/\w+/action$', SurveyPostEFormView.FormToDB,name="survey_postexperiment"),
    url(r'^experiment/survey_postexperiment/(?P<participantid>\w+)/$',SurveyPostEFormView.as_view(),name="survey_postexperiment"),
    
    path('experiment/survey_postexp_webapp',WebapplicationFormView.as_view(),name="survey_postexp_webapp"),
    url(r'^experiment/survey_postexp_webapp/(?P<participantid>\w+)/$',SurveyPostEFormView.as_view(),name="survey_postexp_webapp"),
    
    path('experiment/exp_thanks',TemplateView.as_view(template_name="app3/exp_thanks.html"),name="exp_thanks"),
    
    path('downloaddata', DownloadDataView.as_view(),name='downloaddata'),
    path('downloaddatadetails',TemplateView.as_view(template_name="app3/downloaddata_details.html"),name='downloaddata'),
    
    url(r'^qndata/$',DownloadDataView.questionnairedata,name="qndata"),
    url(r'^viewqndata/$',DownloadDataView.questionnaireview,name="viewqndata"),
    url(r'^viewqnall/$',DownloadDataView.questionnaireviewall,name="viewqnall"),

    url(r'^expdata/$',DownloadDataView.expdata,name="expdata"),
    url(r'^viewexpdata/$',DownloadDataView.expview,name="viewexpdata"),
    url(r'^viewexpdataall/$',DownloadDataView.expviewall,name="viewexpdataall"),

    url(r'^ptdata/$',DownloadDataView.participantdata,name="ptdata"),
    url(r'^viewptdata/$',DownloadDataView.participantview,name="viewptdata"),
    url(r'^viewptdataall/$',DownloadDataView.participantviewall,name="viewptdataall"),

    url(r'^updateexperimentdata$', TaskassignmentExperimentView.updateExperimentData,name='updateexperimentdata'),
    path('full', TaskassignmentFullView.as_view(),name='full'),
    path('members', IndexView.as_view()),
    path('edit',TemplateView.as_view(template_name="app3/edit.html"),name='edit'),
    path('sketch',TemplateView.as_view(template_name="app3/sketch.html")),
    path('formdemo',TemplateView.as_view(template_name="app3/FormDemo.html")),

    path('taskgenerationform',TaskGenerationFormView.as_view(),name="taskgenerationform"),
    url(r'^taskgenerationform/(?P<task_id>\w+)_(?P<subtask_id>\d+)/$',TaskGenerationFormView.as_view(),name="taskgenerationform"),
    path('action_page', TaskGenerationFormView.FormToDB),#.get_values
    url(r'^taskgenerationform/\w+/action_page$',TaskGenerationFormView.FormToDB,name="action_page"),

    path('questionnaireform',QuestionnaireFormView.as_view(),name="questionnaireform"),
    url(r'^questionnaireform/(?P<participant_id>\w+)/(?P<task_id>\w+)/(?P<scene_id>\w+)/$',QuestionnaireFormView.as_view(),name="questionnaireform"),
    path('questionnaire_action', QuestionnaireFormView.FormToDB),
    url(r'^questionnaireform/\w+/\w+/\w+/questionnaire_action$',QuestionnaireFormView.FormToDB,name="questionnaire_action"),

    path('offlinemapdemo',TemplateView.as_view(template_name="app3/offlinemapdemo.html")),
    url(r'^tasksave$',TaskGenerationView.tasksave,name='tasksave'),
    url(r'^gpsupdate$',TaskGenerationView.gpsupdate,name='gpsupdate'),
    url(r'^pathplanningupdate$',TaskGenerationView.pathplanningupdate,name='pathplanningupdate'),
    url(r'^gpshistoricaldataupdate$',TaskGenerationView.gpshistoricaldataupdate,name='gpshistoricaldataupdate'),
    url(r'^getwatershed$',TaskGenerationView.getwatershed,name='getwatershed'),
    url(r'^getsegmentVal$',TaskGenerationView.getSegmentVal,name='getsegmentVal'),
    url(r'^gpsdatastorage$',TaskGenerationView.gpsdatastorage,name='gpsdatastorage'),
    url(r'^demo$',TemplateView.as_view(template_name="app3/demo.html"), name="demo"),
    url(r'^openstreatmap$',TemplateView.as_view(template_name="app3/openstreatmap.html"), name="openstreatmap"),
    url(r'^taskgenerationform/(?P<task_id>\w+)_(?P<subtask_id>\d+)/$',TaskGenerationFormView.as_view(),name="taskgenerationform"),
    url(r'^readfile$',TemplateView.as_view(template_name="app3/readfile.html"), name="readfile"),
    path('api-auth/', include('rest_framework.urls')),
    path('layerquerytest',TemplateView.as_view(template_name="app3/layerquerytest.html")),
    
    url(r'^watershed/$',TemplateView.as_view(template_name="app3/watershed_segmentation.html"),name="watershed"),
    url(r'^watershed/(?P<bobid>\w+)/$',TemplateView.as_view(template_name="app3/watershed_getlinearfeature.html"),name="watershed"),
    path('heatmapringdownload',TemplateView.as_view(template_name="app3/Taskgeneration_download.html")),
    path('videostream',TemplateView.as_view(template_name="app3/UAVVideostream.html")),
    path('index',TaskIndexView.as_view(),name='index'),
    url(r'^getcluemedia$', TaskGenerationView.getClueMedia,name='getcluemedia'),
    path('translateshapefiletogeojson',TemplateView.as_view(template_name="app3/Translate_shapefile_to_geojson.html")),
    path('realdatalocation',TemplateView.as_view(template_name="app3/realdatalocation.html")),
    path('realdatalocationfiltered',TemplateView.as_view(template_name="app3/realdatalocation_filtered.html")),
    path('word',TemplateView.as_view(template_name="app3/words.html")),
    path('words',TemplateView.as_view(template_name="app3/word-spell.html")),
    #path('index',TaskIndexView.asView()),
]

urlpatterns += router.urls
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#print(urlpatterns)
