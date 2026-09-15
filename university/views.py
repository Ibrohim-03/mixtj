from django.shortcuts import render

from django.shortcuts import render
from django.db.models import Avg, Count, Sum
from .models import Student, Grade, Author, Group, Course, Teacher


def task1_students_with_groups(request):
    students = Student.objects.select_related('group')
    return render(request, 'university/task1.html', {'students': students})


def task2_grades_with_students(request):
    grades = Grade.objects.select_related('student', 'subject')
    return render(request, 'university/task2.html', {'grades': grades})


def task3_students_with_grades(request):
    students = Student.objects.prefetch_related('grades', 'grades__subject')
    return render(request, 'university/task3.html', {'students': students})


def task4_authors_with_books(request):
    authors = Author.objects.prefetch_related('books')
    return render(request, 'university/task4.html', {'authors': authors})


def task5_group_student_count(request):
    groups = Group.objects.annotate(student_count=Count('students'))
    return render(request, 'university/task5.html', {'groups': groups})


def task6_student_avg_grade(request):
    students = Student.objects.annotate(avg_score=Avg('grades__score'))
    return render(request, 'university/task6.html', {'students': students})


def task7_author_book_count(request):
    authors = Author.objects.annotate(book_count=Count('books'))
    return render(request, 'university/task7.html', {'authors': authors})


def task8_course_enrollment_count(request):
    courses = Course.objects.annotate(enrollment_count=Count('enrollments'))
    return render(request, 'university/task8.html', {'courses': courses})


def task9_avg_teacher_salary(request):
    result = Teacher.objects.aggregate(avg_salary=Avg('salary'))
    return render(request, 'university/task9.html', {'result': result})


def task10_total_courses_price(request):
    result = Course.objects.aggregate(total_price=Sum('price'))
    return render(request, 'university/task10.html', {'result': result})