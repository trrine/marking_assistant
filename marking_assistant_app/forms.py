from django import forms
from .models import Assignment, Task, Criteria

class AssignmentForm(forms.ModelForm):
    assignment_number = forms.IntegerField(
        label="Assignment Number",
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
    subject_code = forms.CharField(
        label="Subject Code",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    total_marks = forms.DecimalField(
        label="Total Marks",
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )

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
        fields = ["description", "marks", "feedback_comment"]