from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import *
from django.views.generic.base import TemplateView 
from django.views.generic import ListView, DetailView 
import django.views.generic.edit as django_views
from django.forms import ModelForm
from models import *


def portal_home(request):
    # TODO: user type logic
    return render(request, "portal/portal_home.html")

edit_form = "portal/edit_form.html"
class CreateView(django_views.CreateView):
    template_name = edit_form 
    def get_success_url(self):
        return reverse_lazy("portal-home")

class UpdateView(django_views.UpdateView):
    template_name = edit_form
    def get_success_url(self):
        return reverse_lazy("portal-home")
    
# Course
class CourseDetails(DetailView):
    model = Course

class CourseCreate(CreateView):
    model = Course

class CourseList(ListView):
    model = Course

    def get_queryset(self):
        user = self.request.user 
        if user.is_staff:
            return Course.objects.all()

        courses = user.person.taught_courses
        if type(user.person) is Student:
            courses += user.person.courses
        
        return courses.all()

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

# Announcement 
# TODO: restrict to taught courses upon creation / edit 
class AnnouncementDetails(DetailView):
    model = Announcement

class AnnouncementCreate(CreateView):
    model = Announcement
    fields = ['title', 'body', 'course']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AnnouncementCreate, self).form_valid(form)


class AnnouncementList(ListView):
    model = Announcement

    def get_queryset(self):
        user = self.request.user 
        if user.is_staff:
            return Announcement.objects.all()

        announcements = [a for course in user.person.taught_courses for a in course.announcements]
        if type(user.person) is Student:
            announcements += [a for course in user.person.courses for a in course.announcements]
        
        return announcements.all()

class AnnouncementUpdate(UpdateView):
    model = Announcement
    fields = ['title', 'body', 'course']
