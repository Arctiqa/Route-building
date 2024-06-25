from stations.apps import StationsConfig
from django.urls import path

from stations.views import IndexListView

app_name = StationsConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index')
]