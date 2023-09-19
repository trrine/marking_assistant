from django.test import TestCase
from .models import Assignment, Task, Criteria

class AssignmentModelTest(TestCase):
    def setUp(self):
        self.assignment = Assignment.objects.create(
            assignment_number=1,
            subject="Sample Subject",
            total_marks=100.0
        )

    def test_assignment_creation(self):
        self.assertEqual(self.assignment.assignment_number, 1)
        self.assertEqual(self.assignment.subject, "Sample Subject")
        self.assertEqual(self.assignment.total_marks, 100.0)
    
class TaskModelTest(TestCase):
    def setUp(self):
        self.assignment = Assignment.objects.create(
            assignment_number=1,
            subject="Sample Subject",
            total_marks=100.0
        )

        self.task = Task.objects.create(
            assignment=self.assignment,
            task_number=1,
            total_mark=50.0
        )

    def test_task_creation(self):
        self.assertEqual(self.task.task_number, 1)
        self.assertEqual(self.task.total_marks, 50.0)

class CriteriaModelTest(TestCase):
    def setUp(self):
        self.assignment = Assignment.objects.create(
            assignment_number=1,
            subject="Sample Subject",
            total_marks=100.0
        )

        self.task = Task.objects.create(
            assignment=self.assignment,
            task_number=1,
            total_mark=50.0
        )

        self.criteria = Criteria.objects.create(
            task=self.task,
            criteria_number=1,
            description="The code must run with no errors",
            marks=10.0,
            feedback_comment="The code is not running with no errors"
        )

    def test_criteria_creation(self):
        self.assertEqual(self.criteria.criteria_number, 1)
        # OBS
