from django.contrib import admin
from .models import Area, Guide, Excursion, Place, Events, Category, Hotels
admin.site.register(Area)
admin.site.register(Place)
admin.site.register(Category)
admin.site.register(Events)
admin.site.register(Excursion)
admin.site.register(Guide)
admin.site.register(Hotels)