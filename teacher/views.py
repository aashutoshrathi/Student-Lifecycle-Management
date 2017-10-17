from django.shortcuts import render, get_object_or_404

from .models import Teacher, AssignedCourse
from semester.models import Course


def teacher_profile_view(request, teacher_id):
    teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
    courses = AssignedCourse.objects.filter(teacher=teacher)
    all_assigned_courses= []
    for x in courses:
        all_assigned_courses.append(get_object_or_404(Course, code=x.course_code))

    context = {
        'teacher': teacher,
        'all_assigned_courses': all_assigned_courses
    }
    return render(request, 'teacher/teacher.html', context=context)
