from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from portal.models import *

class PersonInline(admin.StackedInline):
    model = Person
    can_delete = False
    verbose_name_plural = 'person'

class UserAdmin(UserAdmin):
    inlines = (PersonInline, )

admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(GradebookEntry)
admin.site.register(Grade)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
