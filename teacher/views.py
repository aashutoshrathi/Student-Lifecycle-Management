from django.shortcuts import render, get_object_or_404

from .models import Teacher


def teacher_profile_view(request, teacher_id):
    teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
    context = {'teacher': teacher}
    return render(request, 'teacher/teacher.html', context=context)
