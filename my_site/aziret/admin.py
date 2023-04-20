from django.contrib import admin
from .models import News, Peoples,Category

# Register your models here.
from . models import *



admin.site.register(Peoples)
admin.site.register(Category)
admin.site.register(News)
admin.site.register(Order)
admin.site.register(Product)