from django.contrib import admin
from device.models import *
@admin.register(Service)
class AdminService(admin.ModelAdmin):
    pass
@admin.register(Address)
class AdminAddress(admin.ModelAdmin):
    pass