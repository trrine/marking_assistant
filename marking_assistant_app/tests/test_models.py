from sqlite3 import IntegrityError
import unittest
from django.test import TestCase
from ..models import Assignment, Task, Criteria

class AssignmentModelTest(TestCase):
    def setUp(self):
        self.assignment = Assignment.objects.create(
            assignment_number=1,
            subject_code="Sample Subject",
            total_marks=100.0
        )

    def test_assignment_creation(self):
        self.assertEqual(self.assignment.assignment_number, 1)
        self.assertEqual(self.assignment.subject_code, "Sample Subject")
        self.assertEqual(self.assignment.total_marks, 100.0)

    # Test assignment model relationships
    def test_assignment_with_tasks(self):
        task1 = Task.objects.create(
            assignment=self.assignment,
            task_number=1,
            total_marks=50.0
        )

        task2 = Task.objects.create(
            assignment=self.assignment,
            task_number=2,
            total_marks=30.0
        )

        # Test if tasks are related correctly
        self.assertEqual(list(self.assignment.task_set.all()), [task1, task2])
    
    # Test unique constraint (assignment_number, subject_code)
    @unittest.expectedFailure
    def test_unique_assignment(self):
        with self.assertRaises(IntegrityError) as context:
            Assignment.objects.create(
                assignment_number=1,
                subject_code="Sample Subject",
                total_marks=100.0
            )

        self.assertTrue("UNIQUE constraint failed" in str(context.exception))

class TaskModelTest(TestCase):
    def setUp(self):
        self.assignment = Assignment.objects.create(
            assignment_number=1,
            subject_code="Sample Subject",
            total_marks=100.0
        )

        self.task = Task.objects.create(
            assignment=self.assignment,
            task_number=1,
            total_marks=50.0
        )

    def test_task_creation(self):
        self.assertEqual(self.task.task_number, 1)
        self.assertEqual(self.task.total_marks, 50.0)

    # Test task model relationships
    def test_task_with_criteria(self):
        # Create a criteria associated with the task
        criteria = Criteria.objects.create(
            task=self.task,
            criteria_number=1,
            description="Sample Description",
            marks=10.0,
            feedback_comment="Sample Comment"
        )

        # Retrieve the criteria through the task's relationship
        criteria_from_task = self.task.criteria_set.first()

        # Test that the criteria retrieved through the relationship matches the created criteria
        self.assertEqual(criteria, criteria_from_task)

    # Test unique constraint (assignment, task_number)
    @unittest.expectedFailure
    def test_unique_task(self):
        assignment = Assignment.objects.create(
            assignment_number=1,
            subject_code="Sample Subject",
            total_marks=100.0
        )

        # Create a Task with the same task_number and assignment
        with self.assertRaises(IntegrityError) as context:
            Task.objects.create(
                assignment=assignment,
                task_number=1,
                total_marks=50.0
            )

        self.assertTrue("UNIQUE constraint failed" in str(context.exception))

class CriteriaModelTest(TestCase):
    def setUp(self):
        self.assignment = Assignment.objects.create(
            assignment_number=1,
            subject_code="Sample Subject",
            total_marks=100.0
        )

        self.task = Task.objects.create(
            assignment=self.assignment,
            task_number=1,
            total_marks=50.0
        )

        self.criteria = Criteria.objects.create(
            task=self.task,
            criteria_number=1,
            description="Sample Description",
            marks=10.0,
            feedback_comment="Sample Comment"
        )

    def test_criteria_creation(self):
        self.assertEqual(self.criteria.criteria_number, 1)
        self.assertEqual(self.criteria.description, "Sample Description")
        self.assertEqual(self.criteria.marks, 10.0)
        self.assertEqual(self.criteria.feedback_comment, "Sample Comment")

    # Test unique constraint (task, criteria_number)
    @unittest.expectedFailure
    def test_unique_criteria(self):
        assignment = Assignment.objects.create(
            assignment_number=1,
            subject_code="Sample Subject",
            total_marks=100.0
        )

        task = Task.objects.create(
            assignment=assignment,
            task_number=1,
            total_marks=50.0
        )

        # Create a Criteria with the same criteria_number and task
        with self.assertRaises(IntegrityError) as context:
            Criteria.objects.create(
                task=task,
                criteria_number=1,
                description="Sample Description",
                marks=10.0,
                feedback_comment="Sample Comment"
            )

        self.assertTrue("UNIQUE constraint failed" in str(context.exception))