from atexit import register
from difflib import context_diff
from django import template
from RecQuiz.models import Lecture,Course,Quiz 
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

@register.inclusion_tag('RecQuiz/course.html')
def get_quiz_list(current_lecture=None):
    context_dict = {}
    try:
        # lecture = Lecture.objects.get(lec_name=current_lecture)
        # quizs = Quiz.objects.filter(Lecture=lecture)
        quizs = Quiz.objects.all()
        context_dict['quizs'] = quizs
    except:
        context_dict['quizs'] = None
    return context_dict

