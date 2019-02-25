from django.urls import path
from django.views.generic import TemplateView
from . import views
from app3.views import IndexView,TaskGenerationView,tasksave
from django.conf.urls import url

urlpatterns = [
    path('', TaskGenerationView.as_view()),
    path('members', IndexView.as_view()),
    path('edit',TemplateView.as_view(template_name="app3/edit.html")),
    path('sketch',TemplateView.as_view(template_name="app3/sketch.html")),
    url(r'^tasksave$',views.tasksave,name='tasksave'),
]
