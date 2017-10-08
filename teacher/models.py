from django.db import models

from django_countries.fields import CountryField


class Teacher(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other'),
    )

    teacher_id = models.CharField(max_length=9, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    contact_number = models.CharField(max_length=10, blank=True, null=True)
    linked_in = models.CharField(max_length=40, blank=True, null=True)
    google_scholars = models.CharField(max_length=50, blank=True, null=True)
    country = CountryField(default='IN')
    state_of_origin = models.CharField(max_length=20, default='Rajasthan', null=True)
    gender = models.CharField(max_length=1, blank=True, null=True, choices=GENDER_CHOICES)
    email = models.CharField(max_length=100, blank=True, null=True)
    qualifications = models.TextField(max_length=100, blank=True, null=True)
    alma_mater = models.CharField(max_length=100, blank=True, null=True)
    areas_of_interest = models.TextField(max_length=1000, blank=True, null=True)
    publications = models.TextField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class AssignedCourse(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=10, blank=True, null=True)
    course_material = models.TextField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.course_code
