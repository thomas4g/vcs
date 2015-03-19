from django.conf.urls import *
from portal.views import *

urlpatterns = patterns('',
    url(r'courses/([\w-]+)/$', CourseView.as_view(), name="course-details"),
    url(r'courses/edit/([\w-]+)/$', CourseUpdate.as_view(), name="course-edit"),
    url(r'courses/$', EnrolledCoursesView.as_view()),
)

