from django.urls import path, include

from . import views
from .views import IndexView
from .views import basket_add, basket_remove
app_name = 'main'

urlpatterns = [
    # path('main', views.main, name='main'),
    path('', IndexView.as_view(), name='index'),
    # path('main', views.main, name='main'),
    path('areas', views.areas, name='areas'),
    path('guides', views.guides, name='guides'),
    # path('areas/area_products', ProductListView.as_view(), name='area_products'),
    path('areas/products/', views.area_products, name='area_products'),
    path('areas/products/category/<int:category_id>/', views.area_category_products, name='area_category_products'),
    path('area/prduct_detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]