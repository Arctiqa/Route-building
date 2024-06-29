from django.views.generic import ListView, TemplateView, CreateView
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from stations.models import Route
from stations.serializers import RouteSerializer


class IndexListView(TemplateView):
    template_name = 'stations/base.html'


class RouteListView(ListView):
    queryset = Route.objects.all()
    template_name = 'stations/route_list.html'


class RouteCreateView(CreateView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    def perform_create(self, serializer):
        route = serializer.save()
        route.owner = self.request.user
        route.save()


class RouteRetrieveAPIView(RetrieveAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class RouteUpdateAPIView(UpdateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class RouteDestroyAPIView(DestroyAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
