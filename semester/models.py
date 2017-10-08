from django.db import models


class Semester(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name = 'Semester'
        verbose_name_plural = 'Semesters'

    STATUS_CHOICES = (
        ('sem1', 'Semester I'),
        ('sem2', 'Semester II'),
        ('sem3', 'Semester III'),
        ('sem4', 'Semester IV'),
        ('sem5', 'Semester V'),
        ('sem6', 'Semester VI'),
        ('sem7', 'Semester VII'),
        ('sem8', 'Semester VIII'),
    )
    name = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Semester I', blank=True, null=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    CLASS_CHOICES = (
        ('th', 'Theory'),
        ('lab', 'LAB'),
    )
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True)
    code = models.CharField(max_length=6, blank=True, null=True)
    days_given = models.IntegerField(blank=True, null=True)
    ref_books = models.TextField(max_length=500, blank=True, null=True)
    is_elective = models.BooleanField(default=False)
    credits = models.IntegerField(default=0, blank=True, null=True)
    classification = models.CharField(max_length=5, default='th', null=True, choices=CLASS_CHOICES)

    def __str__(self):
        return self.code + " : " + self.name


'''
class Quiz:
    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizes'

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, null=True)
    max_marks = models.IntegerField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.title
'''
