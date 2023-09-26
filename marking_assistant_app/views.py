from collections import defaultdict
import os
from django.shortcuts import render, redirect, get_object_or_404

from marking_assistant_app.utils import generate_marking_results_excel
from .forms import AssignmentForm, CriteriaForm, TaskForm
from .models import Assignment, Task, Criteria
from django.forms import modelformset_factory
from django.http import HttpResponse, FileResponse

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


def mark_task_view(request, assignment_id, task_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        # Retrieve the current marking results data from the session
        marking_results_data = request.session.get("marking_results_data", [])

        # Retrieve total marks available for task
        task_marks_total = task.total_marks
        
        # Extract data from the form
        student_number = request.POST.get("student_number")
        criteria_checked = request.POST.getlist("criteria_checked[]")
        extra_comments = request.POST.get("extra_comments").strip()

        # Initialise tasks marks for student
        task_marks = task_marks_total
        feedback_comments = []

        # Go through the criteria for the task and find the ones not met
        for criteria in task.criteria_set.all():
            if str(criteria.id) not in criteria_checked:
                mark_deduction = criteria.marks
                feedback = criteria.feedback_comment
                task_marks -= mark_deduction
                feedback_comments.append(feedback + " (-" + str(mark_deduction) + ").")

        # Add extra comment from user if not empty
        if len(extra_comments) != 0:
            # Add period if needed
            if not extra_comments.endswith("."):
                extra_comments += "."

            feedback_comments.append(extra_comments)
        
        # Add extra feedback based on mark
        if (task_marks / task_marks_total) >= 0.9:
            feedback_comments.append("Good job!")

        elif (task_marks / task_marks_total) >= 0.8:
            feedback_comments.append("Good effort!")
        
        # Marks cannot be less than zero
        elif task_marks < 0:
            task_marks = 0

        # Transform feedback comment list to string
        feedback_string = " ".join(feedback_comments)

        # Save marking results for student
        student_task_results = {
            "subject_code": assignment.subject_code,
            "student_number": str(student_number),
            "assignment_number": str(assignment.assignment_number),
            "task_number": str(task.task_number),
            "marks": str(task_marks),
            "feedback": feedback_string
        }

        # Append the student's results to the marking_results_data
        marking_results_data.append(student_task_results)

        # Update the session with the modified marking_results_data
        request.session["marking_results_data"] = marking_results_data

    return render(request, "mark_task.html", {
        "assignment": assignment,
        "task": task,
    })

def download_results_view(request):
    # Retrieve the marking results data from the session
    marking_results_data = request.session.get("marking_results_data", [])

    if marking_results_data:
        # Generate the Excel file for marking results and save it temporarily on the server
        excel_file_path = generate_marking_results_excel(marking_results_data)

        if os.path.exists(excel_file_path):
            try:
                # Clear the session data
                request.session.pop("marking_results_data")
                
                # Serve the Excel file for download
                return FileResponse(open(excel_file_path, "rb"), as_attachment=True, filename="marking_results.xlsx")
            
            except Exception as e:
                print(e)
                return HttpResponse("Error while serving the file", status=500)
    
    # Handle cases where there are no marking results
    return HttpResponse("No marking results found", status=404)