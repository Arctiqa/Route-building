from django.http import JsonResponse
from django.urls import reverse
from django.views.generic import ListView, TemplateView, CreateView, DetailView
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView

from stations.forms import RouteForm
from stations.models import Route, GasStation
from stations.serializers import RouteSerializer
from stations.utils import get_tomtom_api_build_route


class IndexListView(TemplateView):
    template_name = 'stations/base.html'


class RouteView(ListView):
    model = Route
    template_name = 'stations/route_view.html'


class RouteListView(ListView):
    model = Route
    template_name = 'stations/route_list.html'
    context_object_name = 'route_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class RouteCreateView(CreateView):
    model = Route
    form_class = RouteForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse('stations:route-list')


class RouteDetailView(DetailView):
    model = Route
    template_name = 'stations/route_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        route = self.get_object()
        points = get_tomtom_api_build_route(route)

        context['points'] = points
        if points is not None:
            context['start_point'] = points[0]
        return context


class RouteRetrieveAPIView(RetrieveAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class RouteUpdateAPIView(UpdateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class RouteDestroyAPIView(DestroyAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


def gas_stations(requests):
    stations = GasStation.objects.all().values('latitude', 'longitude', 'number')
    stations_list = list(stations)
    return JsonResponse(stations_list, safe=False)

