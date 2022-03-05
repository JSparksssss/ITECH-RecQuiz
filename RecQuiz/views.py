from difflib import context_diff
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
    #课程页面
    #需要判断首先用户有没有选择这门课程
    #载入课程信息 和 Quiz信息
    course_dict = {
        'name':'Internet Technology',
        'lecture':{
            '1':{    
                'lecture link':'https://itech.blob.core.windows.net/asset-3bb06c3b-2f32-46bc-9e40-a3526c84e51d/CSF-Lecture1.mp4?sp=r&st=2022-02-28T22:04:08Z&se=2022-03-01T06:04:08Z&sv=2020-08-04&sr=b&sig=2o%2F4HSeRaFD5MbAF1qmpHFDt4Gx4%2Flb8x72VCyecrWM%3D',
                'quiz':{
                    '1':{
                        'question':'What is your major?',
                        'answer':{
                            '1':'Computing Science',
                            '2':'Data Science',
                            '3':'Internet Technology',
                            '4':'Computer System Engineering'
                            },
                        'correct answer':'Computer Science',
                        'label':'11:28'

                        }
                    }
                    #有很多Quiz
                }
            }
            #有很多课程
        }
    return render(request,'RecQuiz/course.html',context=course_dict)
def register(request):
    return HttpResponse("This is register page.")
   

#TBC...
#Quiz Report, and other functionalities