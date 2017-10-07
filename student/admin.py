from django.contrib import admin

from .models import Student, RegCourse, CourseQuiz

admin.site.register(Student)
admin.site.register(RegCourse)
admin.site.register(CourseQuiz)
