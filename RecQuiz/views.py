import json
from django.shortcuts import render,redirect
from RecQuiz.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from difflib import context_diff
from RecQuiz.models import Course, Lecture,Quiz,User


# Create your views here.
def index(request):
    #这是一个做判断的页面
    #假设用户已经登陆网页了，那么重定向到myCourse页面；如果用户没有登陆，那么重定向到login界面
    # request.session.set_test_cookie()
    # visitor_cookie_handler(request)
    # print(request.COOKIES.get('is_login'))
    # status = request.COOKIES.get('is_login')  # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    # if not status:
    #     return redirect(reverse('RecQuiz:login'))
    return render(request,'RecQuiz/index.html')

# def index(request):
#     return render(request,'RecQuiz/index.html')

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


def courses(request):
    #显示所有的Course
    context_dict = {}
    try:
        courses = Course.objects.all()
        context_dict['courses'] = courses
    except Course.DoesNotExist:
        context_dict['course'] = None
    
    return render(request,'RecQuiz/courses.html',context = context_dict)

def add_course(request):
    #这里需要实现一个表单request修改数据库的操作
    #用户点击Add To MyCourse可以在Course的外键新增添加一个User的链接

    # if request.method == 'POST':
    #     print("success")
    context_dict = {}
    # user_id = request.COOKIES.get('user_id')
    try:
        # 然后这里的逻辑是筛选用户未选择的课程
        # user = User.objects.get(user_id=user_id)
        # courses = Course.objects.filter(user)

        #这只是为了界面显示而做的操作
        courses = Course.objects.all() 
        context_dict['courses'] = courses
        print("add_course view load data success.")
    except Course.DoesNotExist:
        context_dict['courses'] = None
    return render(request,'RecQuiz/add_course.html',context = context_dict)

        
def course(request,course_name_slug):
    if request.method == 'POST':

        print("success")
    
    # print(course_name_slug)
    context_dict = {}
    try:
        # course = Course.objects.get(slug = course_name_slug)
        # lectures = Lecture.objects.filter(course = course)
        # lecture = lectures.order_by('lec_id').first() 
        # # print("initial lecture id:",lecture.lec_id)    
        # quizs = Quiz.objects.filter(lecture = lecture)
        # context_dict['course'] = course
        # context_dict['lectures'] = lectures
        # context_dict['current_lecture'] = lecture
        # context_dict['quizs'] = quizs
        # context_dict['json_quizs'] = get_quiz_json(request,quizs)
        # print("json-quizs:", context_dict['json_quizs'])
        quizs = Quiz.objects.all()
        context_dict['quizs'] = quizs
        context_dict['json_quizs'] = get_quiz_json(request,quizs)
        print("json-quizs:", context_dict['json_quizs'])
        print("TESTING")
    except Course.DoesNotExist:
        print("Error")
        context_dict['course'] = None
        context_dict['lectures'] = None
        context_dict['current_lecture'] = None
        context_dict['quizs'] = None 

    return render(request,'RecQuiz/quiz.html',context = context_dict)

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
    registered = False
    user_form_errors = ''
    profile_form_errors = ''

    profile_form_errors = ''
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        print ("进入Post")
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        last_name = request.POST.get('last_name', "")
        first_name = request.POST.get('first_name', "")
        email = request.POST.get('first_name', "")
        password = request.POST.get('password', "")
        phone = request.POST.get('phone', "")
        gender = request.POST.get('gender', "")
        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            # user.set_email(user.email)
            # user.set_first_name(user.first_name)
            # user.set_last_name(user.last_name)
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            print (user)

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves,
            # we set commit=False. This delays saving the model
            # until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and
            #put it in the UserProfile model.
            # profile.set_gender(profile.gender)
            # profile.set_phone(profile.phone)
            profile.phone = phone
            profile.gender = gender

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to indicate that the template
            # registration was successful.
            registered = True
        else:
            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            print(user_form.errors, profile_form.errors)
            user_form_errors = user_form.errors
            profile_form_errors = profile_form.errors
    else:
        # Not a HTTP POST, so we render our form using two ModelForm instances.
        # These forms will be blank, ready for user input.
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
                'RecQuiz/register.html',
                context = {'user_form': user_form,
                'profile_form': profile_form,
                'registered': registered,
                'user_form_errors': user_form_errors,
                'profile_form_errors': profile_form_errors,})

def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    login_form_errors = ''
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        # We use request.POST.get('<variable>') as opposed
        # to request.POST['<variable>'], because the
        # request.POST.get('<variable>') returns None if the
        # value does not exist, while request.POST['<variable>']
        # will raise a KeyError exception.
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
        # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                rep = redirect(reverse('RecQuiz:index'))
                rep.set_cookie("is_login", True)
                rep.set_cookie("user_name",)
                return rep
            else:
                # An inactive account was used - no logging in!
                # return HttpResponse("Your Rango account is disabled.")
                login_form_errors = "Your Rango account is disabled."
                return render(request, 'RecQuiz/login.html', context={'login_form_errors': login_form_errors, })
        else:
            # Bad login details were provided. So we can't log the user in.
            print(f"Invalid login details: {username}, {password}")
            login_form_errors = "Invalid login details supplied."
            return render(request, 'RecQuiz/login.html', context={'login_form_errors': login_form_errors, })
            # return HttpResponse("Invalid login details supplied.")
    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'RecQuiz/login.html')

# Use the login_required() decorator to ensure only those logged in can
# access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    rep = redirect(reverse('RecQuiz:login'))
    rep.delete_cookie("is_login")
    # Take the user back to the homepage.
    return rep

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie

    request.session['visits'] = visits
    return HttpResponse("This is register page.")

def get_quiz_json(request,quizs):
    quiz_json = json.dumps(
        [
            {
                'question':quiz.question,
                'choices':[quiz.answer1,quiz.answer2,quiz.answer3,quiz.answer4],
                'correctAnswer':quiz.correct_answer,
                'time':quiz.lecture_time
            }
            for quiz in quizs
        ]
    )
    return quiz_json  
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
#TBC...
#Quiz Report, and other functionalities