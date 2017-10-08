from django.shortcuts import render, get_object_or_404

from .models import Teacher, AssignedCourse


def teacher_profile_view(request, teacher_id):
    teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
    all_assigned_courses = AssignedCourse.objects.filter(teacher=teacher)
    context = {
        'teacher': teacher,
        'all_assigned_courses': all_assigned_courses
    }
    return render(request, 'teacher/teacher.html', context=context)
