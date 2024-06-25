from django.views.generic import ListView, TemplateView


class IndexListView(TemplateView):
    template_name = 'stations/base.html'
