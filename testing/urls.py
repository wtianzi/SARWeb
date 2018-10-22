from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^DuressTesting$',views.DuressTesting,name='DuressTesting'),
    url(r'^DuressTestingAdd$',views.DuressTestingAdd,name='DuressTestingAdd'),
]
