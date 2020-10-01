from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home/home.html'


class WidgetsView(TemplateView):
    template_name = 'widgets.html'


class StackTracesView(TemplateView):
    template_name = 'stack_traces.html'