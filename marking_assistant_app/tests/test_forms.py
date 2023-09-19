from django.test import TestCase
from ..forms import AddAssignmentForm

class AddAssignmentFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            "assignment_number": 1,
            "subject_code": "Sample Subject",
            "total_marks": 100,
            "task_number": [1, 2],
            "task_total_marks": [50, 30],
            "criteria_number": [1, 2],
            "description": ["Sample Desc 1", "Sample Desc 2"],
            "marks": [10, 20],
            "feedback_comment": ["", ""],
        }
        form = AddAssignmentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            "assignment_number": None,  # Missing required field
            "subject_code": "Sample Subject",
            "total_marks": 100,
            # Missing task-related fields
            "task_total_marks": [50, 30],
            "criteria_number": [1, 2],
            "description": ["Sample Desc 1", "Sample Desc 2"],
            "marks": [10, 20],
            "feedback_comment": ["", ""],
        }
        form = AddAssignmentForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_empty_task(self):
        form_data = {
            "assignment_number": 1,
            "subject_code": "Sample Subject",
            "total_marks": 100,
            "task_number": [],
            "task_total_marks": [],
            "criteria_number": [1, 2],
            "description": ["Sample Desc 1", "Sample Desc 2"],
            "marks": [10, 20],
            "feedback_comment": ["", ""],
        }
        form = AddAssignmentForm(data=form_data)
        self.assertTrue(form.is_valid())
