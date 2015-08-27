from django.conf.urls import *
from django.contrib.auth.decorators import login_required
from portal.views import *

urlpatterns = patterns('',
    # course
    url(r'courses/$', CourseList.as_view(), name="course-list"),
    url(r'courses/new/$', CourseCreate.as_view(), name="course-create"),
    url(r'courses/(?P<pk>[\w-]+)/$', CourseDetails.as_view(), name="course-details"),
    url(r'courses/(?P<pk>[\w-]+)/edit$', CourseUpdate.as_view(), name="course-edit"),

    # person
    url(r'persons/$', PersonList.as_view(), name="person-list"),
    
    # parent
    url(r'parents/$', ParentList.as_view(), name="parent-list"),
    url(r'parents/new/$', ParentCreate.as_view(), name="parent-create"),
    url(r'parents/(?P<pk>[\w-]+)/$', ParentDetails.as_view(), name="parent-details"),
    url(r'parents/(?P<pk>[\w-]+)/edit$', ParentUpdate.as_view(), name="parent-edit"),

    # teacher view
    url(r'teachers/(?P<pk>[\w-]+)/$', TeacherDetails.as_view(), name="teacher-details"),

    # student
    url(r'students/$', StudentList.as_view(), name="student-list"),
    url(r'students/new/$', StudentCreate.as_view(), name="student-create"),
    url(r'students/(?P<pk>[\w-]+)/$', StudentDetails.as_view(), name="student-details"),
    url(r'students/(?P<pk>[\w-]+)/edit$', StudentUpdate.as_view(), name="student-edit"),



#    url(r'courses/([\w-]+)/$', CourseView.as_view(), name="course-details"),
#    url(r'courses/edit/([\w-]+)/$', CourseUpdate.as_view(), name="course-edit"),
#    url(r'courses/$', EnrolledCoursesView.as_view()),
#    url(r'courses/([\w-]+)/announcements$', announcement_list),
#    url(r'courses/(?P<course>[\w-]+)/announcements/(?P<pk>[\d]+)/$', announcement_detail),
)

