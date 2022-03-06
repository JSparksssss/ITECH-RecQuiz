from django.urls import path
from RecQuiz import views

app_name = 'RecQuiz'

urlpatterns = [
    path('',views.index,name='index'),
    path('login/', views.login, name='login'),
    path('my_course/',views.my_course,name="my_course"),
    path('new_course/',views.new_course_page,name="new_course_page"),
    path('add_course/',views.add_course,name="add_course"),
    path('course/<slug:course_name_slug>/',views.course,name="course"),
    path('register/',views.register,name="register"),
]