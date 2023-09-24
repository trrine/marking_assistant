from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("add_assignment/", views.add_assignment_view, name="add_assignment"),
    path("manage_assignments/", views.manage_assignments_view, name="manage_assignments"),
    path("start_marking/", views.start_marking_view, name="start_marking"),
    path("edit_assignment/<int:assignment_id>/", views.edit_assignment_view, name="edit_assignment"),
    path("mark_task/<int:assignment_id>/<int:task_id>/", views.mark_task_view, name="mark_task"),
    path("download_results", views.download_results_view, name="download_results"),
]