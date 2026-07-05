from django.urls import path
from .views import (
    dashboard,
    SoldierListView,
    SoldierCreateView,
    SoldierUpdateView,
    SoldierDeleteView,
    PatrolRouteListView,
    PatrolRouteCreateView,
    PatrolRouteUpdateView,
    PatrolRouteDeleteView,
)

urlpatterns = [
    # Soldier URLs
    path('', dashboard, name='dashboard'),
    path('soldiers/', SoldierListView.as_view(), name='soldier_list'),
    path('soldier/add/', SoldierCreateView.as_view(), name='soldier_add'),
    path('soldier/<int:pk>/edit/', SoldierUpdateView.as_view(), name='soldier_edit'),
    path('soldier/<int:pk>/delete/', SoldierDeleteView.as_view(), name='soldier_delete'),

    # Patrol Route URLs
    path('routes/', PatrolRouteListView.as_view(), name='route_list'),
    path('routes/add/', PatrolRouteCreateView.as_view(), name='route_add'),
    path("routes/<int:pk>/edit/", PatrolRouteUpdateView.as_view(), name="route_edit"),
    path("routes/<int:pk>/delete/", PatrolRouteDeleteView.as_view(), name="route_delete"),
]