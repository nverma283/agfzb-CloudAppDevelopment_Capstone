from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(CarMake)
admin.site.register(CarModel)
# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel 
    extra = 5
# CarModelAdmin class
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]

# CarMakeAdmin class with CarModelInline

# Register models here
