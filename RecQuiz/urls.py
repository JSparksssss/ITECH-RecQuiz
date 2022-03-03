from django.urls import path
from RecQuiz import views

app_name = 'RecQuiz'

urlpatterns = [
    path('',views.index,name='index'),
    path('login/', views.login, name='login'),
    path('my_course/',views.my_course,name="my_course"),
    path('add_new_course/',views.add_new_course,name="add_new_course"),
    path('course/',views.course,name="course"),
    path('register/',views.register,name="register"),
]