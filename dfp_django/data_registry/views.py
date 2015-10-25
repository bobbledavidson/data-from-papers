from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.list import ListView
from django.utils import timezone

from data_registry.models import Papers

def index(request):
    return HttpResponse("data regitry index!")


class PaperListView(ListView):

    model = Papers

    def get_context_data(self, **kwargs):
        context = super(PaperListView, self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context

from django.views.generic import list_detail
from django.shortcuts import get_object_or_404

def PaperDetailView(request,paper_id):

    paper = get_object_or_404(Papers, pk=paper_id)

    return list_detail.object_detail(

        request,
        queryset = Papers.objects.all(),
        object_id = author_id,
    )

