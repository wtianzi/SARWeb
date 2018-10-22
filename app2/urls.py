from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blocks', views.blocks, name='index'),
    path('dragpoints', views.dragpoints, name='index'),
    path('lattice', views.lattice, name='index'),
    path('graphs', views.graphs, name='index'),
    path('voronoi', views.voronoi, name='index'),

]
