from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='profile_photos/', blank=True)

class Student(UserProfile):

    pass
class Teacher(UserProfile):

    pass
class Course(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    number_lecture = models.IntegerField()


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    enrollment_date = models.DateTimeField(auto_now_add=True)

class Lecture(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    course_id = models.ForeignKey(Course, on_delete=models.PROTECT)

class Lesson(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    lecture = models.ForeignKey(Lecture, on_delete=models.PROTECT)


# Create your models here.
