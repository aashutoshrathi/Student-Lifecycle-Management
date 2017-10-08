from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from .models import Course, Semester
from student.models import Student, RegCourse
from teacher.models import Teacher, AssignedCourse


def course_view(request, code):
    course = get_object_or_404(Course, code=code)
    assigned_course = get_object_or_404(AssignedCourse, course_code=code)
    registered_courses = RegCourse.objects.filter(course_code=code)
    total_days = course.days_given
    attendance = []
    for i in registered_courses:
        per = ((total_days-i.absent)/total_days)*100
        attendance.append(str(per)[0:5])

    array = zip(registered_courses, attendance)
    context = {
        'course': course,
        'assigned_course': assigned_course,
        'array': array
    }
    return render(request, 'semester/course.html', context=context)
