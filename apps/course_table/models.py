from __future__ import unicode_literals
import re
from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # check course and description length
        if len(postData['courseName']) < 5:
            errors['courseName'] = "Course name should have more than 5 characters"
        if len(postData['description']) < 15:
            errors['description'] = "Course description should have more than 15 characters"
        return errors

class Course(models.Model):
    courseName = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    creeated_at = models.DateTimeField(auto_now_add=True)
    objects = CourseManager()
    def __repr__(self):
        return "Course: --{}".format(self.name)
