from django.contrib import admin
from .models import Soldier, PatrolRoute


@admin.register(Soldier)
class SoldierAdmin(admin.ModelAdmin):
    list_display = (
        'soldier_id',
        'name',
        'rank',
        'posting',
        'status',
        'phone',
    )
    list_filter = ('rank', 'status')
    search_fields = ('soldier_id', 'name', 'phone')


@admin.register(PatrolRoute)
class PatrolRouteAdmin(admin.ModelAdmin):
    list_display = (
        'route_name',
        'area',
        'start_time',
        'end_time',
    )
    search_fields = ('route_name', 'area')