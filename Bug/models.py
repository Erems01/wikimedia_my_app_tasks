from django.db import models

# Create your models here.

class Bug(models.Model):
 # Bug description field
 description = models.TextField()

 # Field for bug type
 BUG_TYPES = [
  ('error', 'Error'),
  ('feature', 'New Feature'),
  ('enhancement', 'Enhancement'),
  ('other', 'Other'),
 ]
 bug_type = models.CharField(max_length=30, choices=BUG_TYPES, default='error')

 # Field for report date
 report_date = models.DateField()

 # Field for bug status
 STATUS_CHOICES = [
  ('todo', 'To Do'),
  ('inprogress', 'In Progress'),
  ('done', 'Done'),
 ]
 status = models.CharField(max_length=30, choices=STATUS_CHOICES,default='todo')

 def __str__(self):
  return self.description 