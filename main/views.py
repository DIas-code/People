from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
from django.contrib.auth.decorators import login_required

# def main(request):
#     return render(request,'main/main.html',{})
class IndexView(TemplateView):
    template_name = 'main/main.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['title'] = 'Sayahat'
        return context

# def areas_