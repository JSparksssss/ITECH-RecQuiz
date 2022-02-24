from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    #这是一个做判断的页面
    #假设用户已经登陆网页了，那么重定向到myCourse页面；如果用户没有登陆，那么重定向到login界面
    return HttpResponse("This is index page.")
    
def login(request):
    return HttpResponse("This is login page.")

def my_course(request):
    return HttpResponse("This is myCourse page.")

def add_new_course(request):
    return HttpResponse("This is add new course page.")

def course(request):
    return HttpResponse("This is course page.")

def register(request):
    return HttpResponse("This is register page.")

#TBC...
#Quiz Report, and other functionalities