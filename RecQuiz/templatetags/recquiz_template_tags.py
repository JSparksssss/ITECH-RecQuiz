from atexit import register
from django import template

register = template.Library()

@register.inclusion_tag('RecQuiz/course.html')
def get_lecture_list(current_course=None):
    #获取这门课程的信息
    return True

@register.inclusion_tag('RecQuiz/mycourse.html')
def get_mycourse_list(current_user=None):
    return True

@register.inclusion_tag('RecQuiz/addnewcourse.html')
def get_newcourse_list(current_user=None):
    return True
