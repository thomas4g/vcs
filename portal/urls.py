from django.conf.urls import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from portal.views import *

urlpatterns = patterns('',
    # course
    url(r'courses/$', CourseList.as_view(), name="course-list"),
    url(r'courses/new/$', staff_member_required(CourseCreate.as_view()), name="course-create"),
    url(r'courses/(?P<pk>[\w-]+)/$', CourseDetails.as_view(), name="course-details"),
    url(r'courses/(?P<pk>[\w-]+)/edit$', CourseUpdate.as_view(), name="course-edit"),

    # person
    url(r'persons/$', PersonList.as_view(), name="person-list"),
    url(r'persons/(?P<pk>[\w-]+)/$', PersonDetails.as_view(), name="person-details"),
    url(r'persons/new/$', staff_member_required(PersonCreate.as_view()), name="person-create"),
    url(r'persons/(?P<pk>[\w-]+)/edit$', staff_member_required(PersonUpdate.as_view()), name="person-edit"),

    # parent
    url(r'parents/$', ParentList.as_view(), name="parent-list"),
    url(r'parents/new/$', staff_member_required(ParentCreate.as_view()), name="parent-create"),
    url(r'parents/(?P<pk>[\w-]+)/$', ParentDetails.as_view(), name="parent-details"),
    url(r'parents/(?P<pk>[\w-]+)/edit$', staff_member_required(ParentUpdate.as_view()), name="parent-edit"),

    # teacher view
    url(r'teachers/(?P<pk>[\w-]+)/$', TeacherDetails.as_view(), name="teacher-details"),

    # student
    url(r'students/$', StudentList.as_view(), name="student-list"),
    url(r'students/new/$', staff_member_required(StudentCreate.as_view()), name="student-create"),
    url(r'students/(?P<pk>[\w-]+)/$', StudentDetails.as_view(), name="student-details"),
    url(r'students/(?P<pk>[\w-]+)/edit$', staff_member_required(StudentUpdate.as_view()), name="student-edit"),

    # announcement
    url(r'announcements/$', AnnouncementList.as_view(), name="announcement-list"),
    url(r'announcements/new/$', AnnouncementCreate.as_view(), name="announcement-create"),
    url(r'announcements/(?P<pk>[\w-]+)/$', AnnouncementDetails.as_view(), name="announcement-details"),
    url(r'announcements/(?P<pk>[\w-]+)/edit$', AnnouncementUpdate.as_view(), name="announcement-edit"),



#    url(r'courses/([\w-]+)/$', CourseView.as_view(), name="course-details"),
#    url(r'courses/edit/([\w-]+)/$', CourseUpdate.as_view(), name="course-edit"),
#    url(r'courses/$', EnrolledCoursesView.as_view()),
#    url(r'courses/([\w-]+)/announcements$', announcement_list),
#    url(r'courses/(?P<course>[\w-]+)/announcements/(?P<pk>[\d]+)/$', announcement_detail),
)

