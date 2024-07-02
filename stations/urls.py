from . import views
from stations.apps import StationsConfig
from django.urls import path

from stations.views import (IndexListView, RouteView, RouteCreateView, RouteListView, RouteDetailView, RouteUpdateView,
                            RouteDeleteView)

app_name = StationsConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('route_view/', RouteView.as_view(), name='route-view'),
    path('route_create/', RouteCreateView.as_view(), name='create-route'),
    path('route_list/', RouteListView.as_view(), name='route-list'),
    path('stations/view/', views.gas_stations, name='gas-stations-view'),
    path('route-detail/<int:pk>/', RouteDetailView.as_view(), name='route-detail'),
    path('route_update/<int:pk>/', RouteUpdateView.as_view(), name='route-update'),
    path('route_delete/<int:pk>/', RouteDeleteView.as_view(), name='route-delete')

]
