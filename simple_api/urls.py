from django.urls import path
from .views.main_view import add_student, get_student, get_student_by_id, update_student, delete_student

urlpatterns = [
    path('add/',add_student, name="add"),
    path('get/',get_student, name="get"),
    path('update/<int:id>/', update_student, name="update"),
    path('get_student_by_id/<int:student_id>/', get_student_by_id, name="get_by_id"),
    path('delete/<int:id>/', delete_student, name="delete"),
]