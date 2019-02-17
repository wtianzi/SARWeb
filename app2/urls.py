from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lattice', views.lattice, name='index'),
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
    path('arcgist',TemplateView.as_view(template_name="app2/ArcGISTriangles.html")),# this is the temporal index
    path('polygonclip',TemplateView.as_view(template_name="app2/polygonclip.html")),
]
