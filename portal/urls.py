from django.conf.urls import *
from portal.views import *

urlpatterns = patterns('',
    url(r'courses/([\w-]+)/$', CourseView.as_view(), name="course-details"),
    url(r'courses/edit/([\w-]+)/$', CourseUpdate.as_view(), name="course-edit"),
    url(r'courses/$', EnrolledCoursesView.as_view()),
    url(r'announcements/$', announcement_list),
    url(r'courses/([\w-]+)/announcements$', announcement_list),
    url(r'courses/(?P<course>[\w-]+)/announcements/(?P<pk>[\d]+)/$', announcement_detail),
    url(r'announcements/([\d]+)/$', announcement_detail),
)

