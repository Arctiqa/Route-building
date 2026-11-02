from django.http import JsonResponse
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, TemplateView, CreateView, DetailView, UpdateView, DeleteView
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from stations.forms import RouteForm
from stations.models import Route, GasStation
from stations.serializers import RouteSerializer
from stations.utils import get_tomtom_api_build_route


class IndexListView(TemplateView):
    template_name = 'stations/base.html'


class RouteView(ListView):
    model = Route
    template_name = 'stations/route_view.html'


class RouteListView(LoginRequiredMixin, ListView):
    model = Route
    template_name = 'stations/route_list.html'
    context_object_name = 'route_list'

    def get_queryset(self):
        return Route.objects.filter(user=self.request.user)


class RouteCreateView(LoginRequiredMixin, CreateView):
    model = Route
    form_class = RouteForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('stations:route-list')


class RouteDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Route
    template_name = 'stations/route_detail.html'

    def test_func(self):
        return self.get_object().user == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        route = self.get_object()

        result = get_tomtom_api_build_route(route)

        if not result:
            context['error'] = 'Не удалось построить маршрут. Проверьте координаты или API-ключ.'
            return context

        points, length_in_meters, travel_time_seconds = result

        stations = GasStation.objects.all().values(
            'latitude', 'longitude', 'number', 'related_service',
            'additional_service', 'diesel_price', 'taneko_diesel_price', 'elevation'
        )

        context['stations'] = list(stations)
        context['points'] = points
        context['lengthInMeters'] = int(length_in_meters / 1000)
        context['travelTimeInSeconds'] = round(int(travel_time_seconds) / 3600, 1)
        context['start_point'] = points[0]

        return context


class RouteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Route
    form_class = RouteForm

    def test_func(self):
        return self.get_object().user == self.request.user

    def get_success_url(self):
        return reverse('stations:route-list')


class RouteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Route

    def test_func(self):
        return self.get_object().user == self.request.user

    def get_success_url(self):
        return reverse('stations:route-list')


class RouteCreateAPIView(CreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class RouteRetrieveAPIView(RetrieveAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class RouteUpdateAPIView(UpdateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class RouteDestroyAPIView(DestroyAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


def gas_stations(request):
    stations = GasStation.objects.all().values('latitude', 'longitude', 'number')
    return JsonResponse(list(stations), safe=False)