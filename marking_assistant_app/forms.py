# forms.py
from django import forms
from .models import Assignment

class CombinedForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ["assignment_number", "subject", "total_mark"]

    # Additional fields for Task and Criteria
    task_number = forms.CharField()
    task_total_mark = forms.DecimalField()
    criteria_number = forms.CharField()
    description = forms.CharField()
    marks = forms.DecimalField()
    feedback_comment = forms.CharField()
