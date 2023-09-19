from django import forms
from .models import Assignment, Task, Criteria

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ["assignment_number", "subject_code", "total_marks"]

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["task_number", "total_marks"]

class CriteriaForm(forms.ModelForm):
    class Meta:
        model = Criteria
        fields = ["criteria_number", "description", "marks", "feedback_comment"]
