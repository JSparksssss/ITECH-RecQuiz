import json
from difflib import context_diff
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from RecQuiz.models import Course, Lecture,Quiz,User
# Create your views here.
def index(request):
    #这是一个做判断的页面
    #假设用户已经登陆网页了，那么重定向到myCourse页面；如果用户没有登陆，那么重定向到login界面
    return render(request,'RecQuiz/index.html')

def login(request):
    return render(request,'RecQuiz/login.html')

# #这个view层可以放到下方的courses，用if user.islogin
# def my_course(request):
#     context_dict = {}
#     try:
#         # user = User.objects.get(slug=user_id_slug)
#         # course = Course.objects.filter(User=user)
#         courses = Course.objects.all()
#         context_dict['courses'] = courses
#     except Course.DoesNotExist:
#         context_dict['course'] = None
    
#     return render(request, 'RecQuiz/my_course.html', context = context_dict)


def courses(request):
    #应该能够筛选出用户未注册的course
    context_dict = {}
    try:
        # user = User.objects.get(slug=user_id_slug)
        # course = Course.objects.filter(User=user)
        courses = Course.objects.all()
        context_dict['courses'] = courses
    except Course.DoesNotExist:
        context_dict['course'] = None
    
    return render(request,'RecQuiz/courses.html',context = context_dict)


#这个view层可以实现新增课程的操作
def add_course(request):
    if request.method == 'POST':
        print("success")
    return render(request,'RecQuiz/add_course.html')

#Fetch the lecture and quiz related to the         
def course(request,course_name_slug):
    context_dict = {}
    try:
        course = Course.objects.get(slug = course_name_slug)
        lectures = Lecture.objects.filter(course = course)
        lecture = lectures.order_by('lec_id').first() 
        print("initial lecture id:",lecture.lec_id)    
        quizs = Quiz.objects.filter(lecture = lecture)
        context_dict['course'] = course
        context_dict['lectures'] = lectures
        context_dict['current_lecture'] = lecture
        context_dict['quizs'] = quizs
        context_dict['json_quizs'] = get_quiz_json(request,quizs)
        return render(request,'RecQuiz/course.html',context = context_dict)
    except:
        context_dict['course'] = None
        context_dict['lectures'] = None
        context_dict['current_lecture'] = None
        context_dict['quizs'] = None  

    return render(request,'RecQuiz/course.html',context = context_dict)

def lecture(request,course_name_slug,lec_id):
    context_dict = {}
    try:
        course = Course.objects.get(slug = course_name_slug)
        lectures = Lecture.objects.filter(course = course)
        lecture = lectures.get(lec_id=lec_id) 
        print("current lecture id",lecture.lec_id)    
        quizs = Quiz.objects.filter(lecture = lecture)
        context_dict['course'] = course
        context_dict['lectures'] = lectures
        context_dict['current_lecture'] = lecture
        context_dict['quizs'] = quizs
        context_dict['json_quizs'] = get_quiz_json(request,quizs)
        return render(request,'RecQuiz/course.html',context = context_dict)
    except:
        context_dict['course'] = None
        context_dict['lectures'] = None
        context_dict['current_lecture'] = None
        context_dict['quizs'] = None  

    return render(request,'RecQuiz/course.html',context = context_dict)

def register(request):
    return HttpResponse("This is register page.")
   
def about(request):
    return render(request,'RecQuiz/about.html')

def contact(request):
    return render(request,'RecQuiz/contact.html')

def pricing(request):
    return render(request,'RecQuiz/pricing.html')

def trainers(request):
    return render(request,'RecQuiz/trainers.html')
    
def events(request):
    return render(request,'RecQuiz/events.html')


def get_quiz_json(request,quizs):
    quiz_json = json.dumps(
        [
            {
                'question':quiz.Question,
                'choices':[quiz.Answer1,quiz.Answer2,quiz.Answer3,quiz.Answer4],
                'correctAnswer':quiz.correct_answer
            }
            for quiz in quizs
        ]
    )
    return quiz_json

#TBC...
#Quiz Report, and other functionalities
