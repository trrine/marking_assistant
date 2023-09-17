from django.shortcuts import render

def index_view(request):
    return render(request, "index.html")

def add_assignment_view(request):
    return render(request, "add.html")

def manage_assignments_view(request):
    return render(request, "manage.html")

def start_marking_view(request):
    return render(request, "marking.html")