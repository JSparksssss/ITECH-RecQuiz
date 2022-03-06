from difflib import context_diff
from django.http import HttpResponse
from django.shortcuts import render
from RecQuiz.models import Course, Lecture,User
# Create your views here.
def index(request):
    #这是一个做判断的页面
    #假设用户已经登陆网页了，那么重定向到myCourse页面；如果用户没有登陆，那么重定向到login界面
    return render(request,'RecQuiz/index.html')
    
def login(request):
    return HttpResponse("This is login page.")

def my_course(request):
    context_dict = {}
    try:
        # user = User.objects.get(slug=user_id_slug)
        # course = Course.objects.filter(User=user)
        courses = Course.objects.all()
        context_dict['courses'] = courses
    except Course.DoesNotExist:
        context_dict['course'] = None
    
    return render(request, 'RecQuiz/my_course.html', context = context_dict)


def new_course_page(request):
    #应该能够筛选出用户未注册的course
    context_dict = {}
    try:
        # user = User.objects.get(slug=user_id_slug)
        # course = Course.objects.filter(User=user)
        courses = Course.objects.all()
        context_dict['courses'] = courses
    except Course.DoesNotExist:
        context_dict['course'] = None
    
    return render(request,'RecQuiz/new_course.html',context = context_dict)

def add_course(request):
    if request.method == 'POST':
        print("success")
    return render(request,'RecQuiz/add_course.html')

        
def course(request,course_name_slug):
    context_dict = {}
    try:
        course = Course.objects.get(slug = course_name_slug)
        lectures = Lecture.objects.filter(course = course)
        context_dict['course'] = course
        context_dict['lecutres'] = lectures
    except:
        context_dict['course'] = course
        context_dict['lecutres'] = lectures
    return render(request,'RecQuiz/course.html',context = context_dict)

def register(request):
    return HttpResponse("This is register page.")
   

#TBC...
#Quiz Report, and other functionalities