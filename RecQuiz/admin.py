from django.contrib import admin
from RecQuiz.models import UserProfile

from RecQuiz.models import User, Course, Lecture, Quiz

class UserAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('user_id',)}
    list_display = ('user_id','psw','email_id','first_name','last_name','gender','phone_number')
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('course_name',)}
    list_display = ('course_id','coordinator','course_name')
class LectureAdmin(admin.ModelAdmin):
    list_display = ('course','url','lec_id','lec_name','length','content')
class QuizAdmin(admin.ModelAdmin):
    list_display = ('lecture','quiz_id','question','answer1','answer2','answer3','answer4','correct_answer','lecture_time')

admin.site.register(User,UserAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Lecture,LectureAdmin)
admin.site.register(Quiz,QuizAdmin)
# Register your models here.

admin.site.register(UserProfile)