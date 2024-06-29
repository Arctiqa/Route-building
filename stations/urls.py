from stations.apps import StationsConfig
from django.urls import path

from stations.views import IndexListView, RouteListView

app_name = StationsConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('route_view', RouteListView.as_view(), name='route'),
    path('route_list', RouteListView.as_view(), name='route-list'),


]