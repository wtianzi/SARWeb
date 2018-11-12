from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blocks', views.blocks, name='index'),
    path('dragpoints', views.dragpoints, name='index'),
    path('lattice', views.lattice, name='index'),
    path('graphs', views.graphs, name='index'),
    path('voronoi', views.voronoi, name='index'),
    path('mvoronoi', views.multilinevoronoi, name='index'),
    path('circle', views.circle, name='index'),
    path('d3v3voronoi', views.d3v3voronoi, name='index'),
    path('arcgis', views.arcgis, name='index'),
    path('arcgisc', views.arcgisc, name='index'),
    path('arcgisv', views.arcgisv, name='index'),
]
