from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("add_assignment/", views.add_assignment_view, name="add_assignment"),
    path("manage_assignments/", views.manage_assignments_view, name="manage_assignments"),
    path("start_marking/", views.start_marking_view, name="start_marking"),
]