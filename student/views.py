from django.shortcuts import render, get_object_or_404
import datetime
from .models import Student, RegCourse
from semester.models import Course


def get_programme_name(student_programme):
    if student_programme == 'ug_cse':
        return 'B.Tech. (CSE)'
    elif student_programme == 'ug_it':
        return 'B.Tech. (IT)'
    elif student_programme == 'pg_cse':
        return 'M.Tech. (CSE)'
    elif student_programme == 'pg_it':
        return 'M.Tech. (IT)'


def get_gender(gender):
    if gender == 'm':
        return 'Male'
    elif gender == 'f':
        return 'Female'
    else:
        return 'Other'


def get_sem(id):
    t = datetime.datetime.now()
    enrolled_year = int(id[0:4])
    cur_year = t.year
    year = cur_year-enrolled_year
    if year > 4:
        return "Graduated"
    else:
        sem = year*2+2
    if t.month >= 8:
        sem -= 1
    return sem


def retrieve_course_obj(course_code):
    return get_object_or_404(Course, code=course_code)


def ret_sem(str_sem):
    return "Semester" + str_sem[3:4]


def student_view(request, pk):
    student_profile = get_object_or_404(Student, student_id=pk)
    student_profile.programme = get_programme_name(student_profile.programme)
    student_profile.gender = get_gender(student_profile.gender)
    context = {
        'student_profile': student_profile,
    }
    return render(request, 'studentProfile.html', context=context)


def academic_view(request, pk):
    student_profile = get_object_or_404(Student, student_id=pk)
    courses = RegCourse.objects.all().filter(student=student_profile)
    student_profile.programme = get_programme_name(student_profile.programme)
    student_profile.gender = get_gender(student_profile.gender)
    sem = get_sem(student_profile.student_id)
    course_detail = []
    for course in courses:
        tmp_course = retrieve_course_obj(course.course_code)
        abss = course.absent
        per = (tmp_course.days_given - abss) / tmp_course.days_given
        tmp_grade = course.grade
        temp = (str(per*100)[0:5], abss, tmp_course, tmp_grade)
        course_detail.append(temp)

    context = {
        'student_profile': student_profile,
        'sem': sem,
        'courses': courses,
        'course_detail': course_detail,
    }
    return render(request, 'AcademicDetails.html', context=context)


def fee_view(request, pk):
    student_profile = get_object_or_404(Student, student_id=pk)

    context = {
        'student_profile': student_profile,
    }
    return render(request, 'fees.html', context=context)


def application_view(request, pk):
    student_profile = get_object_or_404(Student, student_id=pk)

    context = {
        'student_profile': student_profile,
    }
    return render(request, 'Applications.html', context=context)


def event_view(request, pk):
    student_profile = get_object_or_404(Student, student_id=pk)

    context = {
        'student_profile': student_profile,
    }
    return render(request, 'Events.html', context=context)
