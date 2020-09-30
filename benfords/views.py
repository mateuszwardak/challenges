from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView

from benfords.core import handle_input_file
from benfords.forms import DataSetForm
from benfords.models import DataSet


class DatasetsView(TemplateView):
    template_name = 'benfords/datasets.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                'datasets': DataSet.objects.all().order_by('-created_at'),
            },
        )
        return context


class DatasetView(TemplateView):
    template_name = 'benfords/dataset.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        dataset = DataSet.objects.get(pk=kwargs.get('pk'))
        context.update(
            {
                'dataset': dataset,
            }
        )

        return context


class NewDataSetView(CreateView):
    model = DataSet
    form_class = DataSetForm
    template_name = 'benfords/new_dataset.html'

    def get_success_url(self):
        return reverse('benfords:datasets')

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        result_graph = handle_input_file(self.object.input_file)
        self.object.result_graph.save('result_graph.png', result_graph, save=False)
        self.object.save()
        return HttpResponseRedirect(reverse_lazy('benfords:dataset', args=[self.object.pk]))


