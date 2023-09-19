from decimal import Decimal
from django.test import TestCase
from django.urls import reverse
from ..models import Assignment, Task, Criteria

class AddAssignmentViewTestCase(TestCase):
    def setUp(self):
        # Set up initial data for the forms
        self.assignment_data = {
            "assignment_number": "1",
            "subject_code": "ABC123",
            "total_marks": "100.00",
        }

        self.task_data = {
            "task_number": "1",
            "total_marks": "50.00",
        }

        self.criteria_data = {
            "criteria_number": "1",
            "description": "Sample Criteria",
            "marks": "25.00",
            "feedback_comment": "Good job!",
        }

    def test_add_assignment_view(self):
        # Check that the view returns a 200 OK response
        response = self.client.get(reverse("add_assignment"))
        self.assertEqual(response.status_code, 200)

    def test_add_assignment(self):
        # Check that a new assignment, task, and criteria are saved in the database
        assignment_count_before = Assignment.objects.count()
        task_count_before = Task.objects.count()
        criteria_count_before = Criteria.objects.count()

        response = self.client.post(reverse("add_assignment"), {
            **self.assignment_data,
            "task_number[]": [self.task_data["task_number"]],
            "task_total_marks[]": [self.task_data["total_marks"]],
            "criteria_number[]": [self.criteria_data["criteria_number"]],
            "description[]": [self.criteria_data["description"]],
            "marks[]": [self.criteria_data["marks"]],
            "feedback_comment[]": [self.criteria_data["feedback_comment"]],
        })

        assignment_count_after = Assignment.objects.count()
        task_count_after = Task.objects.count()
        criteria_count_after = Criteria.objects.count()

        self.assertEqual(response.status_code, 302)  # Check for a redirect
        self.assertEqual(assignment_count_after, assignment_count_before + 1)  # Check assignment count
        self.assertEqual(task_count_after, task_count_before + 1)  # Check task count
        self.assertEqual(criteria_count_after, criteria_count_before + 1)  # Check criteria count

        # Check that the newly created assignment has the expected values
        new_assignment = Assignment.objects.latest("id")
        self.assertEqual(new_assignment.assignment_number, int(self.assignment_data["assignment_number"]))
        self.assertEqual(new_assignment.subject_code, self.assignment_data["subject_code"])
        self.assertEqual(new_assignment.total_marks, Decimal(self.assignment_data["total_marks"]))

        # Check that the newly created task and criteria are associated with the assignment
        new_task = Task.objects.latest("id")
        self.assertEqual(new_task.assignment, new_assignment)
        self.assertEqual(new_task.task_number, int(self.task_data["task_number"]))  
        self.assertEqual(new_task.total_marks, Decimal(self.task_data["total_marks"]))  

        new_criteria = Criteria.objects.latest("id")
        self.assertEqual(new_criteria.task, new_task)
        self.assertEqual(new_criteria.criteria_number, int(self.criteria_data["criteria_number"]))  
        self.assertEqual(new_criteria.description, self.criteria_data["description"])
        self.assertEqual(new_criteria.marks, Decimal(self.criteria_data["marks"]))  
        self.assertEqual(new_criteria.feedback_comment, self.criteria_data["feedback_comment"])