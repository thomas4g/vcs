from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import *
from django.views.generic.base import TemplateView 
from django.views.generic import ListView, DetailView, DeleteView
import django.views.generic.edit as django_views
from django.forms import ModelForm, DateInput
from django.forms.widgets import HiddenInput
from models import *


class DateInput(DateInput):
    input_type = 'date'

class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'
        widgets = {
            'deadline': DateInput(),
            'late_deadline': DateInput()
        }

def portal_home(request):
    context = {}
    # TODO: user type logic
    if request.user.is_staff and request.GET.get('plain', '') != '1':
        context['announcements'] = Announcement.objects.all()
        context['courses'] = Course.objects.all()
        context['students'] = Student.objects.all()
        context['users'] = User.objects.all()
        return render(request, "portal/admin_home.html", context)
    else:
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
    fields = ['title', 'description', 'teacher', 'students', 'year', 'period']

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

class CourseDelete(DeleteView):
    model = Course

# Assignment
class AssignmentDetails(DetailView):
    model = Assignment

class AssignmentCreate(CreateView):
    model = Assignment
    form_class = AssignmentForm

    def get_form(self, request, **kwargs):
        form = super(AssignmentCreate, self).get_form(request, **kwargs)
        form.fields['course'].widget = HiddenInput()
        form.initial = {"course": self.kwargs["course"]}
        return form

class AssignmentList(ListView):
    model = Assignment

    def get_queryset(self):
        user = self.request.user 
        course = Course.objects.get(slug=self.kwargs["course"])
        if user.person.taught_courses.filter(slug=course.slug).exists():
            if type(user.person) is Student:
                if user.person.enrolled_courses.filter(slug=course.slug).exists():
                    # TODO FAIL here
                    pass

        assignments = course.assignments
        return assignments.all()

    def get_context_data(self, **kwargs):
        context = super(AssignmentList, self).get_context_data(**kwargs)
        context['course'] = Course.objects.get(slug=self.kwargs["course"])
        return context

class AssignmentUpdate(UpdateView):
    model = Assignment

# User
class UserDetails(DetailView):
    model = User

class UserDelete(DeleteView):
    model = User

class UserCreate(CreateView):
    model = User
    fields = ['username', 'password', 'first_name', 'last_name', 'email']

class UserList(ListView):
    model = User

class UserUpdate(UpdateView):
    model = User
    fields = ['username', 'password', 'first_name', 'last_name', 'email']

# Teacher
class TeacherDetails(DetailView):
    model = User 
    template_name = "portal/teacher_detail.html"


# Student
class StudentDetails(DetailView):
    model = Student

class StudentCreate(UserCreate):
    model = Student
    def __init__(self):
        self.fields = self.fields + ['parents']

class StudentList(ListView):
    model = Student

class StudentUpdate(UserUpdate):
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

class AnnouncementDelete(DeleteView):
    model = Announcement
    fields = ['title', 'body', 'course']
