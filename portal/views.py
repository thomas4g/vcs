from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import *
from django.views.generic.base import TemplateView 
from django.views.generic import ListView, DetailView, UpdateView
from models import *

def announcement_list(request, course=None):
    announcements = Announcement.objects.all() if course is None else Announcement.objects.filter(course__slug=course)
    return render(request, 'portal/announcements.html', {'announcements': announcements})

def announcement_detail(request, pk, course=None):
    return render(request, 'portal/announcement.html', {'object':
        get_object_or_404(Announcement, pk=pk, course__slug=course)})

class CourseView(DetailView):
    template_name = 'portal/course.html'
    
    def get_object(self):
        return get_object_or_404(Course, slug=self.args[0])

class CourseUpdate(UpdateView):
    model = Course
    fields = ["description"]    
    def get_object(self):
        return get_object_or_404(Course, slug=self.args[0])
    def get_success_url(self):
        success_url = reverse_lazy("course-details", args=[self.args[0]])
        return success_url

class EnrolledCoursesView(ListView):
    model = Course
    template_name = 'portal/courses.html'

    def get_queryset(self):
        return self.request.user.person.enrollments.all()
