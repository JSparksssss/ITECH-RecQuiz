from django.contrib import admin

from RecQuiz.models import User, Course, Lecture, Quiz

class UserAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('user_id',)}
    list_display = ('user_id','psw','email_id','first_name','last_name','gender','phone_number')
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('course_name',)}
    list_display = ('course_id','coordinator','course_name')



admin.site.register(User,UserAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Lecture)
admin.site.register(Quiz)
# Register your models here.
