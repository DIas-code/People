from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
from django.contrib.auth.decorators import login_required

class IndexView(TemplateView):
    template_name = 'main/main.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['title'] = 'Sayahat'
        return context

def areas(request):
    return render(request, 'main/areas.html',{})

def guides(request):
    return render(request, 'main/guides.html',{})

def CategoryListView(request):
    return render(request, 'main/area_products.html',{})

def HotelsView(request):
    ...

def EventsView(request):
    ...

def ExcursionView(request):
    ...