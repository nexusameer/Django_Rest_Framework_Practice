from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('student', views.post_student, name='post_student'),
    path('update_student/<int:id>', views.update_student, name='update_student'),
    path('delete_student/<int:id>', views.delete_student, name='delete_student'),
    path('get_books', views.get_books, name= 'get_books')
]