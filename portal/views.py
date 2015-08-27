from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import *
from django.views.generic.base import TemplateView 
from django.views.generic import ListView, DetailView 
import django.views.generic.edit as django_views
from django.forms import ModelForm
from models import *

edit_form = "portal/edit_form.html"
class CreateView(django_views.CreateView):
    template_name = edit_form 
    def get_success_url(self):
        return reverse_lazy(self.model.__name__.lower() + "-list")

class UpdateView(django_views.UpdateView):
    template_name = edit_form
    def get_success_url(self):
        return reverse_lazy(self.model.__name__.lower() + "-details", args=[self.args[0]])


# Course
class CourseDetails(DetailView):
    model = Course

class CourseCreate(CreateView):
    model = Course

class CourseList(ListView):
    model = Course

class CourseUpdate(UpdateView):
    model = Course

# Person
class PersonDetails(DetailView):
    model = Person

class PersonCreate(CreateView):
    model = Person
    fields = ['username', 'password', 'first_name', 'last_name', 'email']

class PersonList(ListView):
    model = Person

class PersonUpdate(UpdateView):
    model = Person
    fields = ['username', 'password', 'first_name', 'last_name', 'email']

# Teacher
class TeacherDetails(DetailView):
    model = Person 
    template_name = "portal/teacher_detail.html"


# Parent
class ParentDetails(DetailView):
    model = Parent

class ParentCreate(PersonCreate):
    model = Parent

class ParentList(ListView):
    model = Parent

class ParentUpdate(PersonUpdate):
    model = Parent

# Student
class StudentDetails(DetailView):
    model = Student

class StudentCreate(PersonCreate):
    model = Student
    def __init__(self):
        self.fields = self.fields + ['parents']

class StudentList(ListView):
    model = Student

class StudentUpdate(PersonUpdate):
    model = Student
    def __init__(self):
        self.fields = self.fields + ['parents']
