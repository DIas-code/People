from django.urls import path, include

from . import views
from .views import IndexView
app_name = 'main'

urlpatterns = [
    # path('main', views.main, name='main'),
    path('', IndexView.as_view(), name='index'),
    # path('main', views.main, name='main'),
    path('areas', views.areas, name='areas'),
    path('guides', views.guides, name='guides'),
]