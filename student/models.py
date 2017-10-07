from django.db import models


class Student(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other'),
    )

    name = models.CharField(max_length=30, blank=True, null=True)
    contact_number = models.CharField(max_length=10, blank=True, null=True)
    guardians_number = models.CharField(max_length=10, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    address = models.TextField(max_length=100, blank=True, null=True)
    blood_group = models.CharField(max_length=3, blank=True, null=True)
    student_id = models.CharField(max_length=9, blank=True, null=True)
    application_number = models.CharField(max_length=9, blank=True, null=True)
    programme = models.CharField(max_length=9, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True, choices=GENDER_CHOICES)

    def __str__(self):
        return self.student_id


class RegCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=10, blank=True, null=True)
    attendance = models.IntegerField(blank=True, null=True)
    grade = models.CharField(max_length=4, blank=True, null=True)

    def __str__(self):
        return self.course_code


class CourseQuiz(models.Model):
    course = models.ForeignKey(RegCourse, on_delete=models.CASCADE)
    marks_obtained = models.CharField(max_length=6, blank=True, null=True)
