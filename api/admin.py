
from django.contrib import admin
from .models import Hospitals, Want, Districts

class HospitalAdmin(admin.ModelAdmin):
    list_display = ('hospital',)

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('district',)

admin.site.register(Hospitals, HospitalAdmin)  
admin.site.register(Districts, DistrictAdmin) 
admin.site.register(Want)