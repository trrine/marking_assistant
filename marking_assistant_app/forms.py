# forms.py
from django import forms
from .models import Assignment

class CombinedForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ["assignment_number", "subject_code", "total_marks"]

    # Additional fields for Task and Criteria
    task_number = forms.CharField()
    task_total_marks = forms.DecimalField()
    criteria_number = forms.CharField()
    description = forms.CharField()
    marks = forms.DecimalField()
    feedback_comment = forms.CharField()
