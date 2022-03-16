from django.urls import path,re_path
from RecQuiz import views

app_name = 'RecQuiz'
#http://127.0.0.1:8000/recquiz/course/cyber-security-fundamentals/
urlpatterns = [
    path('',views.index,name='index'),
    path('logout/', views.user_logout, name='logout'),
    path('about/',views.about,name='about'),
    path('login/', views.user_login, name='login'),
    path('my_course/',views.my_course,name="my_course"),
    path('courses/',views.courses,name="courses"),
    path('add_course/',views.add_course,name="add_course"),
    path('course/<slug:course_name_slug>/',views.unbind,name="course"),
    path('register/',views.register,name="register"),
    path('contact/',views.contact,name="contact"),
    path('pricing/',views.pricing,name="pricing"),
    path('trainers/',views.trainers,name="trainers"),
    path('events/',views.events,name="events"),
    #path('course/<slug:course_name_slug>',views.unbind,name="unbind"),
]