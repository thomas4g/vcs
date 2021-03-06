from __future__ import division
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from utils import get_letter_grade
from datetime import datetime
from ckeditor.fields import RichTextField


class Student(User):
    parents = models.ManyToManyField(User, related_name='children')
    class Meta:
        verbose_name = 'Student'


class Course(models.Model):
    title = models.CharField(max_length=150)
    description = RichTextField()
    slug = models.CharField(primary_key=True, max_length=50, unique=True)
    teacher = models.ForeignKey(User, related_name='taught_courses')
    students = models.ManyToManyField(Student, blank=True, related_name='enrolled_courses')
    YEAR_CHOICES = map(lambda x: (x,x), range(1970, datetime.now().year + 1))
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.now().year)
    period = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __unicode__(self):
        return self.title

    def get_course_grade(self, student):
        return sum([grade.get_weighted_points() for entry in self.graded_items.all() for grade in entry.grades.all() if grade.student == student]) / 100.



class Announcement(models.Model):
    title = models.CharField(max_length=150)
    body = RichTextField()
    author = models.ForeignKey(User, related_name='announcements')
    course = models.ForeignKey(Course, related_name='announcements', null=True, blank=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['modified']

class GradebookEntry(models.Model):
    course = models.ForeignKey(Course, related_name="graded_items")
    title = models.CharField(max_length=150)
    description = RichTextField()
    max_points = models.IntegerField(default=100)
    weight = models.FloatField(default=1, validators=[MinValueValidator(0), MaxValueValidator(1)])
    class Meta:
        verbose_name_plural = "Gradebook Entries"


class Assignment(GradebookEntry):
    _course = models.ForeignKey(Course, null=True, blank=True, editable=False, related_name='assignments')
    deadline = models.DateTimeField()
    late_deadline = models.DateTimeField(blank=True)
    proctored = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self._course = self.course
        if not self.late_deadline:
            self.late_deadline = self.deadline
        return super(Assignment, self).save(*args, **kwargs)

class Grade(models.Model):
    entry = models.ForeignKey(GradebookEntry, related_name='grades')
    student = models.ForeignKey(Student, related_name='grades')
    points = models.IntegerField()
    comments = models.TextField()

    def get_weighted_points(self):
        return self.points * self.entry.weight

    def get_percentage_grade(self):
        return self.points / self.entry.max_points

    def get_letter_grade(self):
        return get_letter_grade(self.get_percentage_grade())

    def __unicode__(self):
        return str(self.get_percentage_grade() * 100) + '%'

class Attachment(models.Model):
    author = models.ForeignKey(User, related_name='attachments')
    course = models.ForeignKey(Course, related_name='attachments', null=True, blank=True)
    assignment = models.ForeignKey(Assignment, related_name='attachments', null=True, blank=True)
    file = models.FileField()

    def save(self, *args, **kwargs):
        if self.assignment and self.assignment.course is not self.course:
            raise ValidationError("Assignment must match course")
        return super(Attachment, self).save(*args, **kwargs)


