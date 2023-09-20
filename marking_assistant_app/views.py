from django.shortcuts import render, redirect, get_object_or_404
from .forms import AssignmentForm, CriteriaForm, TaskForm
from .models import Assignment, Task, Criteria
from django.forms import modelformset_factory

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

            return redirect("index")  # Redirect after submission

    else:
        # Initialize an empty AssignmentForm for GET requests
        assignment_form = AssignmentForm()

    return render(request, "add.html", {"assignment_form": assignment_form})

def manage_assignments_view(request):
    # Retrieve a list of existing assignments
    assignments = Assignment.objects.all()
    
    return render(request, "manage.html", {"assignments": assignments})

def edit_assignment_view(request, assignment_id):
    # Get the assignment object based on the assignment_id
    assignment = get_object_or_404(Assignment, id=assignment_id)

    # Initialise empty formsets for tasks and criteria
    TaskFormSet = modelformset_factory(Task, form=TaskForm, extra=0)
    CriteriaFormSet = modelformset_factory(Criteria, form=CriteriaForm, extra=0)

    # Check if the request is a POST (form submission)
    if request.method == "POST":
        # Populate the assignment form with POST data
        assignment_form = AssignmentForm(request.POST, instance=assignment)
        task_formset = TaskFormSet(request.POST, queryset=Task.objects.filter(assignment=assignment))
        criteria_formset = CriteriaFormSet(request.POST, queryset=Criteria.objects.filter(task__assignment=assignment))

        # Check if all forms are valid
        if assignment_form.is_valid() and task_formset.is_valid() and criteria_formset.is_valid():
            # Save the assignment form
            assignment_form.save()

            # Save the task and criteria formsets
            task_formset.save()
            criteria_formset.save()

            # Redirect to manage assignments page
            return redirect("manage_assignments")

    else:
        # Populate the assignment form with existing assignment data
        assignment_form = AssignmentForm(instance=assignment)
        task_formset = TaskFormSet(queryset=Task.objects.filter(assignment=assignment))
        criteria_formset = CriteriaFormSet(queryset=Criteria.objects.filter(task__assignment=assignment))

    return render(request, "edit.html", {
        "assignment_form": assignment_form,
        "task_formset": task_formset,
        "criteria_formset": criteria_formset,
    })

def start_marking_view(request):
    return render(request, "marking.html")