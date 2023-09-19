from django.test import TestCase
from ..forms import AssignmentForm, TaskForm, CriteriaForm

class AssignmentFormTest(TestCase):
    def test_assignment_form_valid(self):
        data = {
            "assignment_number": 1,
            "subject_code": "ABC123",
            "total_marks": 100.00
        }
        form = AssignmentForm(data=data)
        self.assertTrue(form.is_valid())

    def test_assignment_form_invalid(self):
        data = {}  # Invalid data, required fields missing
        form = AssignmentForm(data=data)
        self.assertFalse(form.is_valid())

class TaskFormTest(TestCase):
    def test_task_form_valid(self):
        data = {
            "task_number": 1,
            "total_marks": 50.00
        }
        form = TaskForm(data=data)
        self.assertTrue(form.is_valid())

    def test_task_form_invalid(self):
        data = {}  # Invalid data, required fields missing
        form = TaskForm(data=data)
        self.assertFalse(form.is_valid())

class CriteriaFormTest(TestCase):
    def test_criteria_form_valid(self):
        data = {
            "criteria_number": 1,
            "description": "Test Criteria",
            "marks": 10.00,
            "feedback_comment": "Good job!"
        }
        form = CriteriaForm(data=data)
        self.assertTrue(form.is_valid())

    def test_criteria_form_invalid(self):
        data = {}  # Invalid data, required fields missing
        form = CriteriaForm(data=data)
        self.assertFalse(form.is_valid())
