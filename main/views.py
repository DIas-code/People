from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Area, Category, Products
# Create your views here.
from django.contrib.auth.decorators import login_required

class IndexView(TemplateView):
    template_name = 'main/main.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['title'] = 'Sayahat'
        return context

def areas(request):
    context = {
            'title': 'sayahat',
            'areas': Area.objects.all(),
        }
    return render(request, 'main/areas.html', context)

def guides(request):
    return render(request, 'main/guides.html',{})


class ProductListView(ListView):
    model = Products
    template_name = 'main/area_products.html'

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data()
        context['title'] = 'Sayahat'
        context['categories'] = Category.objects.all()
        return context