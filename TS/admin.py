from django.contrib.gis import admin
from .models import User, POI, StayPoint, Trace

# Register your models here.

# admin.register(WorldBorder, admin.GeoModelAdmin)

admin.site.site_header = 'Trajectory Data Manager'
admin.site.site_title = 'Secret of Trace'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'name', 'email']
    ordering = ['user_id']


@admin.register(POI)
class POIAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'address']
    list_per_page = 50
    search_fields = ['name']
    list_filter = ['type']
    ordering = ['id']


@admin.register(StayPoint)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ['id', 'start_time', 'end_time']
    list_per_page = 50


@admin.register(Trace)
class TDAdmin(admin.ModelAdmin):
    list_display = ['id', 'start_time', 'end_time']
    list_per_page = 50

