from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from portal.models import *

admin.site.register(Course)
admin.site.register(Announcement)
admin.site.register(Attachment)
admin.site.register(GradebookEntry)
admin.site.register(Assignment)
admin.site.register(Grade)
admin.site.register(Student)
