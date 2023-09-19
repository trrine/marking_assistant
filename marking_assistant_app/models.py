from django.db import models

class Assignment(models.Model):
    assignment_number = models.PositiveIntegerField(default=1)
    subject_code = models.TextField()
    total_marks = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ("assignment_number", "subject_code")

class Task(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    task_number = models.PositiveIntegerField(default=1)
    total_marks = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ("assignment", "task_number")

class Criteria(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    criteria_number = models.PositiveIntegerField(default=1)
    description = models.TextField()
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    feedback_comment = models.TextField()

    class Meta:
        unique_together = ("task", "criteria_number")