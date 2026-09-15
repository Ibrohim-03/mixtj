from django.urls import path
from . import views

urlpatterns = [
    path('task1/', views.task1_students_with_groups, name='task1'),
    path('task2/', views.task2_grades_with_students, name='task2'),
    path('task3/', views.task3_students_with_grades, name='task3'),
    path('task4/', views.task4_authors_with_books, name='task4'),
    path('task5/', views.task5_group_student_count, name='task5'),
    path('task6/', views.task6_student_avg_grade, name='task6'),
    path('task7/', views.task7_author_book_count, name='task7'),
    path('task8/', views.task8_course_enrollment_count, name='task8'),
    path('task9/', views.task9_avg_teacher_salary, name='task9'),
    path('task10/', views.task10_total_courses_price, name='task10'),
]