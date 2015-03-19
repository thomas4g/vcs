from __future__ import division
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from utils import get_letter_grade
from datetime import datetime


class Person(models.Model):
    user = models.OneToOneField(User, related_name="person")
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

class Course(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    slug = models.CharField(max_length=50, primary_key=True)
    teacher = models.ForeignKey(Person, related_name='taught_courses')
    students = models.ManyToManyField(Person, through='Enrollment')
    YEAR_CHOICES = map(lambda x: (x,x), range(1970, datetime.now().year + 1))
    year = models.IntegerField(max_length=4, choices=YEAR_CHOICES, default=datetime.now().year)
    period = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __unicode__(self):
        return self.title

class GradebookEntry(models.Model):
    course = models.ForeignKey(Course)
    title = models.CharField(max_length=150)
    description = models.TextField()
    max_points = models.IntegerField()  
    weight = models.FloatField(default=1, validators=[MinValueValidator(0), MaxValueValidator(1)])


# class Assignment(GradebookEntry):
#     # deadline

class Grade(models.Model):
    entry = models.ForeignKey(GradebookEntry)
    student = models.ForeignKey(Person, related_name='grades')
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


class Enrollment(models.Model):
    person = models.ForeignKey(Person, related_name="enrollments")
    course = models.ForeignKey(Course)
    
    def get_grade(self):
        max_points = 0
        points = 0
        print ""
        for grade in self.person.grades.filter(entry__course=self.course):
            points += grade.points * grade.entry.weight
            max_points += grade.entry.max_points * grade.entry.weight
        return points / max_points
    def get_letter_grade(self):
        return get_letter_grade(self.get_grade()) 
    

