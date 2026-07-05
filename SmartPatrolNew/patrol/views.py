from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Soldier, PatrolRoute

def dashboard(request):
    context = {
        "total_soldiers": Soldier.objects.count(),
        "on_duty": Soldier.objects.filter(status="On Duty").count(),
        "on_leave": Soldier.objects.filter(status="Leave").count(),
        "total_routes": PatrolRoute.objects.count(),
    }

    return render(request, "dashboard.html", context)

# Soldier Views
class SoldierListView(ListView):
    model = Soldier
    template_name = "soldiers.html"
    context_object_name = "soldiers"


class SoldierCreateView(CreateView):
    model = Soldier
    fields = [
        "soldier_id",
        "name",
        "age",
        "rank",
        "blood_group",
        "phone",
        "status",
        "photo",
    ]
    template_name = "add_soldier.html"
    success_url = reverse_lazy("soldier_list")


class SoldierUpdateView(UpdateView):
    model = Soldier
    fields = [
        "soldier_id",
        "name",
        "age",
        "rank",
        "blood_group",
        "phone",
        "status",
        "photo",
    ]
    template_name = "add_soldier.html"
    success_url = reverse_lazy("soldier_list")


class SoldierDeleteView(DeleteView):
    model = Soldier
    template_name = "delete_soldier.html"
    success_url = reverse_lazy("soldier_list")


# Patrol Route Views
class PatrolRouteListView(ListView):
    model = PatrolRoute
    template_name = "routes.html"
    context_object_name = "routes"


class PatrolRouteCreateView(CreateView):
    model = PatrolRoute
    fields = ["route_name", "area", "start_time", "end_time"]
    template_name = "routes.html"
    success_url = reverse_lazy("route_list")
class PatrolRouteUpdateView(UpdateView):
    model = PatrolRoute
    fields = ["route_name", "area", "start_time", "end_time"]
    template_name = "routes.html"
    success_url = reverse_lazy("route_list")


class PatrolRouteDeleteView(DeleteView):
    model = PatrolRoute
    template_name = "delete_route.html"
    success_url = reverse_lazy("route_list")