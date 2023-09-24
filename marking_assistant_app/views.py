from collections import defaultdict
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
            description_data = request.POST.getlist("description[]")
            marks_data = request.POST.getlist("marks[]")
            feedback_comment_data = request.POST.getlist("feedback_comment[]")
            task_for_criteria_data = request.POST.getlist("task_for_criteria[]")

            # Create a dictionary to group criteria by task_number
            criteria_by_task = defaultdict(list)
            for i in range(len(description_data)):
                task_number = task_for_criteria_data[i]
                criteria_by_task[task_number].append({
                    "description": description_data[i],
                    "marks": marks_data[i],
                    "feedback_comment": feedback_comment_data[i]
                })

            for i in range(len(task_data)):
                task_number = task_data[i]
                task_total_marks = task_total_marks_data[i]

                # Create a Task instance and associate it with the assignment
                task = Task.objects.create(
                    assignment=assignment,
                    task_number=task_number,
                    total_marks=task_total_marks
                )

                # Iterate through the relevant criteria for this task
                for criteria_data in criteria_by_task.get(task_number, []):
                    description = criteria_data["description"]
                    marks = criteria_data["marks"]
                    feedback_comment = criteria_data["feedback_comment"]

                    # Create a Criteria instance and associate it with the task
                    Criteria.objects.create(
                        task=task,
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
    assignment = get_object_or_404(Assignment, id=assignment_id)
    TaskFormSet = modelformset_factory(Task, form=TaskForm, extra=0)
    CriteriaFormSet = modelformset_factory(Criteria, form=CriteriaForm, extra=0)

    if request.method == "POST":
        if "delete_assignment" in request.POST:
            # Handle deletion of the entire assignment
            assignment.delete()
            return redirect("manage_assignments")  # Redirect to the index page after deletion

        assignment_form = AssignmentForm(request.POST, instance=assignment)

        if assignment_form.is_valid():
            assignment = assignment_form.save()

            # Handle tasks and criteria creation
            task_numbers = request.POST.getlist("task_number[]")
            task_total_marks_list = request.POST.getlist("task_total_marks[]")
            task_ids = request.POST.getlist("task_id[]")
            criteria_descriptions = request.POST.getlist("description[]")
            criteria_marks_list = request.POST.getlist("marks[]")
            criteria_feedback_comments = request.POST.getlist("feedback_comment[]")
            criteria_ids = request.POST.getlist("criteria_id[]")
            task_for_criteria = request.POST.getlist("task_for_criteria[]")

            # Create a dictionary to group criteria by task_number
            criteria_by_task = defaultdict(list)
            for i in range(len(criteria_descriptions)):
                task_number = task_for_criteria[i]
                criteria_by_task[task_number].append({
                    "description": criteria_descriptions[i],
                    "marks": criteria_marks_list[i],
                    "feedback_comment": criteria_feedback_comments[i],
                    "id": criteria_ids[i]
                })

            # Retrieve task IDs from the database and form data
            task_ids_db = set(Task.objects.filter(assignment=assignment).values_list("id", flat=True))
            task_ids_form = set(int(task_id) for task_id in task_ids if task_id)  # Convert form data to a set of integers

            # Find task IDs in the database but not in the form data
            tasks_to_delete = task_ids_db.difference(task_ids_form)

            # Delete tasks that are in the 'tasks_to_delete' set
            Task.objects.filter(id__in=tasks_to_delete).delete()

            for i in range(len(task_numbers)):
                task_number = task_numbers[i]
                task_total_marks = task_total_marks_list[i]

                task, created = Task.objects.update_or_create(
                    assignment=assignment,
                    task_number=task_number,
                    defaults={
                        "total_marks": task_total_marks
                    }
                )

                # Iterate through the relevant criteria for this task
                for criteria_data in criteria_by_task.get(task_number, []):
                    description = criteria_data["description"]
                    marks = criteria_data["marks"]
                    feedback_comment = criteria_data["feedback_comment"]
                    id = criteria_data["id"]

                    # Check if id is an empty string and handle it accordingly
                    if id == "":
                        id = None

                    # Create a Criteria instance and associate it with the task
                    criteria, created = Criteria.objects.update_or_create(
                        task=task,  # Filter criteria for matching the task
                        id=id,  # Additional filter criteria
                        defaults={
                            "description": description,
                            "marks": marks,
                            "feedback_comment": feedback_comment
                        }
                    )

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
    # Retrieve a list of existing assignments
    assignments = Assignment.objects.all()
    
    return render(request, "marking.html", {"assignments": assignments})


def mark_assignment_view(request, assignment_id):
    return render(request, "mark_assignment.html")