from django.conf.urls import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from portal.views import *

urlpatterns = [ 
    # home
    url(r'home/$', portal_home, name='portal-home'),

    # course
    url(r'courses/$', CourseList.as_view(), name="course-list"),
    url(r'courses/new/$', staff_member_required(CourseCreate.as_view()), name="course-create"),
    url(r'courses/(?P<pk>[\w-]+)/$', CourseDetails.as_view(), name="course-details"),
    url(r'courses/(?P<pk>[\w-]+)/edit$', CourseUpdate.as_view(), name="course-edit"),
    url(r'courses/(?P<pk>[\w-]+)/delete$', CourseDelete.as_view(), name="course-delete"),

    # assignment
    url(r'courses/(?P<course>[\w-]+)/assignments/$', AssignmentList.as_view(), name="assignment-list"),
    url(r'courses/(?P<course>[\w-]+)/assignments/new/$', staff_member_required(AssignmentCreate.as_view()), name="assignment-create"),
    url(r'assignments/(?P<pk>[\d]+)/$', AssignmentDetails.as_view(), name="assignment-details"),
    url(r'assignments/(?P<pk>[\w-]+)/edit$', AssignmentUpdate.as_view(), name="assignment-edit"),


    # person
    url(r'users/$', UserList.as_view(), name="user-list"),
    url(r'users/new/$', staff_member_required(UserCreate.as_view()), name="user-create"),
    url(r'users/(?P<pk>[\w-]+)/$', UserDetails.as_view(), name="user-details"),
    url(r'users/(?P<pk>[\w-]+)/edit$', staff_member_required(UserUpdate.as_view()), name="user-edit"),
    url(r'users/(?P<pk>[\w-]+)/delete$', staff_member_required(UserDelete.as_view()), name="user-delete"),

    # teacher view
    url(r'teachers/(?P<pk>[\w-]+)/$', TeacherDetails.as_view(), name="teacher-details"),

    # student
    url(r'students/$', StudentList.as_view(), name="student-list"),
    url(r'students/new/$', staff_member_required(StudentCreate.as_view()), name="student-create"),
    url(r'students/(?P<pk>[\w-]+)/$', StudentDetails.as_view(), name="student-details"),
    url(r'students/(?P<pk>[\w-]+)/edit$', staff_member_required(StudentUpdate.as_view()), name="student-edit"),
    url(r'students/(?P<pk>[\w-]+)/delete$', staff_member_required(UserDelete.as_view()), name="student-delete"),

    # announcement
    url(r'announcements/$', AnnouncementList.as_view(), name="announcement-list"),
    url(r'announcements/new/$', AnnouncementCreate.as_view(), name="announcement-create"),
    url(r'announcements/(?P<pk>[\w-]+)/$', AnnouncementDetails.as_view(), name="announcement-details"),
    url(r'announcements/(?P<pk>[\w-]+)/edit$', AnnouncementUpdate.as_view(), name="announcement-edit"),
    url(r'announcements/(?P<pk>[\w-]+)/delete$', AnnouncementDelete.as_view(), name="announcement-delete"),



#    url(r'courses/([\w-]+)/$', CourseView.as_view(), name="course-details"),
#    url(r'courses/edit/([\w-]+)/$', CourseUpdate.as_view(), name="course-edit"),
#    url(r'courses/$', EnrolledCoursesView.as_view()),
#    url(r'courses/([\w-]+)/announcements$', announcement_list),
#    url(r'courses/(?P<course>[\w-]+)/announcements/(?P<pk>[\d]+)/$', announcement_detail),
]
