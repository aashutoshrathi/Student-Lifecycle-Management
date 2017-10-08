from django.db import models

from django_countries.fields import CountryField
import datetime


class Student(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))

    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other'),
    )

    BG_CHOICES = (
        ('a+', 'A+'),
        ('b+', 'B+'),
        ('ab', 'AB'),
        ('ab+', 'AB+'),
        ('o', 'O'),
        ('o+', 'O+'),
        ('o-', 'O-'),
    )

    CATEGORY_CHOICES = (
        ('gen', 'General'),
        ('obc', 'OBC'),
        ('sc', 'SC'),
        ('st', 'ST'),
        ('pwd', 'PwD'),
    )

    PRG_CHOICES = (
        ('ug_cse', 'B.Tech.(CS)'),
        ('ug_it', 'B.Tech.(IT)'),
        ('pg_cs', 'M.Tech.(CS)'),
        ('pg_it', 'M.Tech.(IT)'),
    )

    student_id = models.CharField(max_length=9, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    contact_number = models.CharField(max_length=10, blank=True, null=True)
    guardians_number = models.CharField(max_length=10, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(max_length=100, blank=True, null=True)
    blood_group = models.CharField(max_length=3, blank=True, null=True, choices=BG_CHOICES)
    application_number = models.CharField(max_length=9, blank=True, null=True)
    programme = models.CharField(max_length=10, default='ug_cse', null=True, choices=PRG_CHOICES)
    gender = models.CharField(max_length=1, blank=True, null=True, choices=GENDER_CHOICES)
    social_category = models.CharField(max_length=3, default='gen', null=True, choices=CATEGORY_CHOICES)
    email = models.CharField(max_length=100, blank=True, null=True)
    aadhar = models.CharField(max_length=16, blank=True, null=True)
    country = CountryField(default='IN')
    state_of_origin = models.CharField(max_length=20, default='Rajasthan', null=True)
    # default = CBSE
    qualifying_board = models.CharField(max_length=100, default='Central Board of Secondary Education', null=True)
    # default = 10 + 2
    qualifying_exam = models.CharField(max_length=100, blank=True,null=True)
    qualifying_exam_percentage = models.CharField(max_length=100, blank=True,null=True)
    qualifying_exam_year = models.IntegerField(choices=YEAR_CHOICES, null=True, default=datetime.datetime.now().year)

    def __str__(self):
        return self.student_id


class RegCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=10, blank=True, null=True)
    absent = models.IntegerField(blank=True, null=True)
    grade = models.CharField(max_length=4, blank=True, null=True)
    instructor_remarks = models.TextField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.course_code


class CourseQuiz(models.Model):
    course = models.ForeignKey(RegCourse, on_delete=models.CASCADE)
    marks_obtained = models.CharField(max_length=6, blank=True, null=True)
