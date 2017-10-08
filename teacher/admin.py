from django.contrib import admin

from .models import Teacher, AssignedCourse

admin.site.register(Teacher)
admin.site.register(AssignedCourse)