from django.urls import path
from django.views.generic import TemplateView
from . import views
from app3.views import IndexView,TaskGenerationView

urlpatterns = [
    path('', TaskGenerationView.as_view()),
    path('/members', IndexView.as_view()),
]
