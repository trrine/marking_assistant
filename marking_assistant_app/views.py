from django.shortcuts import render, redirect
from .forms import CombinedForm
from .models import Assignment, Task, Criteria

def index_view(request):
    return render(request, "index.html")

def add_assignment_view(request):
    if request.method == "POST":
        combined_form = CombinedForm(request.POST)
        if combined_form.is_valid():
            # Save Assignment
            assignment = combined_form.save()

            # Process and save multiple tasks and criteria
            task_numbers = request.POST.getlist("task_number[]")
            task_total_marks = request.POST.getlist("task_total_mark[]")
            criteria_numbers = request.POST.getlist("criteria_number[]")
            descriptions = request.POST.getlist("description[]")
            marks = request.POST.getlist("marks[]")
            feedback_comments = request.POST.getlist("feedback_comment[]")

            for i in range(len(task_numbers)):
                task = Task(
                    assignment=assignment,
                    task_number=task_numbers[i],
                    total_mark=task_total_marks[i]
                )
                task.save()

                criteria = Criteria(
                    task=task,
                    criteria_number=criteria_numbers[i],
                    description=descriptions[i],
                    marks=marks[i],
                    feedback_comment=feedback_comments[i]
                )
                criteria.save()

            # Redirect to index
            return redirect("index_view")
    else:
        combined_form = CombinedForm()

    return render(request, "add.html", {"combined_form": combined_form})

def manage_assignments_view(request):
    return render(request, "manage.html")

def start_marking_view(request):
    return render(request, "marking.html")