from django.db import models

from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    group = models.ForeignKey(
        Group, 
        on_delete=models.CASCADE, 
        related_name='students'
    )

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Subject(models.Model):
    title = models.CharField(max_length=50)
    hours = models.IntegerField()

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    student = models.ForeignKey(
        Student, 
        on_delete=models.CASCADE, 
        related_name='enrollments'
    )
    course = models.ForeignKey(
        Course, 
        on_delete=models.CASCADE, 
        related_name='enrollments'
    )
    enrolled_at = models.DateField(auto_now_add=True)


class Grade(models.Model):
    student = models.ForeignKey(
        Student, 
        on_delete=models.CASCADE, 
        related_name='grades'
    )
    subject = models.ForeignKey(
        Subject, 
        on_delete=models.CASCADE, 
        related_name='grades'
    )
    score = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.subject.title}: {self.score}"


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        related_name='books'
    )

    def __str__(self):
        return self.title


class Library(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name