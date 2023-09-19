from django.shortcuts import render, redirect
from .forms import AssignmentForm, CriteriaForm, TaskForm
from .models import Assignment, Task, Criteria

def index_view(request):
    return render(request, "index.html")

def add_assignment_view(request):
    if request.method == "POST":
        # Handle the assignment form
        assignment_form = AssignmentForm(request.POST)

        if assignment_form.is_valid():
            assignment = assignment_form.save()  # Save the assignment

            # Handle tasks and criteria creation
            task_data = request.POST.getlist("task_number[]")
            task_total_marks_data = request.POST.getlist("task_total_marks[]")
            criteria_data = request.POST.getlist("criteria_number[]")
            description_data = request.POST.getlist("description[]")
            marks_data = request.POST.getlist("marks[]")
            feedback_comment_data = request.POST.getlist("feedback_comment[]")

            for i in range(len(task_data)):
                task_number = task_data[i]
                task_total_marks = task_total_marks_data[i]

                # Create a Task instance and associate it with the assignment
                task = Task.objects.create(
                    assignment=assignment,
                    task_number=task_number,
                    total_marks=task_total_marks
                )

                for j in range(len(criteria_data)):
                    criteria_number = criteria_data[j]
                    description = description_data[j]
                    marks = marks_data[j]
                    feedback_comment = feedback_comment_data[j]

                    # Create a Criteria instance and associate it with the task
                    criteria = Criteria.objects.create(
                        task=task,
                        criteria_number=criteria_number,
                        description=description,
                        marks=marks,
                        feedback_comment=feedback_comment
                    )

            return redirect("index_view")  # Redirect to a success page after submission

    else:
        # Initialize an empty AssignmentForm for GET requests
        assignment_form = AssignmentForm()

    return render(request, "add.html", {"assignment_form": assignment_form})

def manage_assignments_view(request):
    return render(request, "manage.html")

def start_marking_view(request):
    return render(request, "marking.html")