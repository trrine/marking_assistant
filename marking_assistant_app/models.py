from django.db import models

class Assignment(models.Model):
    assignment_number = models.PositiveIntegerField(default=1)
    subject = models.TextField()
    total_mark = models.DecimalField(max_digits=5, decimal_places=2)

class Task(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    task_number = models.PositiveIntegerField(default=1)
    total_mark = models.DecimalField(max_digits=5, decimal_places=2)

class Criteria(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    criteria_number = models.PositiveIntegerField(default=1)
    description = models.TextField()
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    feedback_comment = models.TextField()