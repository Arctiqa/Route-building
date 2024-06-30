from django.contrib import admin

from stations.models import Route, GasStation

admin.site.register(Route)
admin.site.register(GasStation)
