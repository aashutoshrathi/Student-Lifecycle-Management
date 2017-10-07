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

    MARITAL_STATUS = (
        ('m', 'Married'),
        ('u', 'Unmarried'),
    )

    name = models.CharField(max_length=30, blank=True, null=True)
    student_id = models.CharField(max_length=9, blank=True, null=True)

    def __str__(self):
        return self.student_id


class Reg(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=10, blank=True, null=True)
    attendance = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.course_code
