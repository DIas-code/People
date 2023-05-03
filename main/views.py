from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Area, Category, Products, Basket
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


# class ProductListView(ListView):
#     model = Products
#     template_name = 'main/area_products.html'
#
#     def get_queryset(self):
#         queryset = super(ProductListView, self).get_queryset()
#         category_id = self.kwargs.get('category_id')
#         return queryset.filter(category_id=category_id) if category_id else queryset
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super(ProductListView, self).get_context_data()
#         context['title'] = 'Sayahat'
#         context['categories'] = Category.objects.all()
#         return context

def area_products(request, area_id):
    products = Products.objects.filter(area_id=area_id)
    categories = Category.objects.all()
    context = {'products': products,
               'categories': categories
               }
    return render(request, 'main/area_products.html', context)

def area_category_products(request, area_id, category_id):
    products = Products.objects.filter(area_id=area_id, category_id=category_id)
    categories = Category.objects.all()
    context = {'products': products,
               'categories': categories
               }
    return render(request, 'main/area_products.html', context)

@login_required
def basket_add(request, product_id):
    product = Products.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, products=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, products=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    print(request)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, product_id):
    # if self.products.category == "Events":
    #         return self.products.events.price * self.quantity
    #     elif self.products.category == "Excursions":
    #         return self.products.excursion.price * self.quantity
    #     return self.products.hotels.price * self.quantity
    product = Products.events.get(id=product_id)

    basket = Basket.objects.filter(user = request.user, products = product)
    
    basket.remove(product)
