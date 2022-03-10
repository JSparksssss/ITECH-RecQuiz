import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','RecQuiz_project.settings')

import django
django.setup()
from RecQuiz.models import User, Course, Lecture, Quiz

def populate():
    quiz_page1 = [{'quiz_id':1, 'question':'What is not the target of this course?',
                'answer1':'To defend the web attacks','answer2':'To attack others',
                'answer3':'To learn cyber security','answer4':'To realize the data tranfer through website',
                'correct_answer':'To attack others','lecture_time':5}]
    quiz_page2 = [{'quiz_id':1, 'question':'Personal Data and COnfidential documents needs to be protected',
                'answer1':'True','answer2':'False','answer3':'NONE','answer4':'NONE',
                'correct_answer':'True','lecture_time':708},
                {'quiz_id':2, 'question':'MAC address is the definitive address of Network Interface Card(NIC). Unique for every host',
                'answer1':'True','answer2':'False','answer3':'NONE','answer4':'NONE',
                'correct_answer':'True','lecture_time':832},
                {'quiz_id':3, 'question':'What is one of the main reasons that cyber security risk is higher as the years go by? Please choose only one answer, the one that fits best',
                'answer1':'Because we rely more and more on networking infrastructures','answer2':'Because there is good defence mechanisms',
                'answer3':'Because there is lots of research regarding the improvement of cyber security','answer4':'Because we are spending more resources on increasing cyber security awareness',
                'correct_answer':'Because we rely more and more on networking infrastructures','lecture_time':1368}]
    quiz_page3 =[{'quiz_id':1, 'question':'Web science is a course related to crawling data from website',
                'answer1':'True','answer2':'False','answer3':'NONE','answer4':'NONE',
                'correct_answer':'True','lecture_time':10}]
    quiz_page4 = [{'quiz_id':0, 'question':'Not availale',
                'answer1':'Not availale','answer2':'Not availale','answer3':'Not availale','answer4':'Not availale',
                'correct_answer':'Not availale','lecture_time':0}]



    lecture_page1 = {
        1001:{'quiz_page':quiz_page1, 'lec_name':'CSF_1','url':'https://drive.google.com/uc?export=view&id=1SMqJ1XnnUQ4M6LRAp4JsruZYptgTSelm', 
        'content':'CSF_1','length':0},
        1002:{'quiz_page':quiz_page2, 'lec_name':'CSF_2','url':'https://drive.google.com/uc?export=view&id=1n0_a3vN4W1Cq69yRoE8AF17HY3sFHsrQ', 
        'content':'CSF_2','length':0},
        1003:{'quiz_page':quiz_page4, 'lec_name':'CSF_3','url':'https://drive.google.com/uc?export=view&id=1vWJLKK-LVrGJJDfOIkYSLKWlwmzTE0LS', 
        'content':'CSF_3','length':0},
        1004:{'quiz_page':quiz_page4, 'lec_name':'CSF_4','url':'https://drive.google.com/uc?export=view&id=1_RgKGmEL5Ro0-I98rT3itPZA_XxhyQLX', 
        'content':'CSF_4','length':0}   
    }
    lecture_page2 = {
        2001:{'quiz_page':quiz_page3, 'lec_name':'WS_1','url':'https://drive.google.com/uc?export=view&id=1PAsshNOuben3oHnD2AwtAhMNX5IrzYv1', 
        'content':'WS_1','length':0},
        2002:{'quiz_page':quiz_page4, 'lec_name':'WS_2','url':'https://drive.google.com/uc?export=view&id=1aYXEaAyYv1MO-GVlT0pOoKYAc_n9N5Kr', 
        'content':'WS_2','length':0}, 
    }
    lecture_page3 = {
        6789:{'quiz_page':quiz_page4,'lec_name':'not available','url':'not available', 
        'content':'NONE','length':0 }
    }

    course_pages1 = {
        4062: {'lec_page':lecture_page1, 'course_name':'Cyber Security Fundamentals', 'coordinator':'Maria Evangelopoulou'},
        5060: {'lec_page':lecture_page3,'course_name':'Human-Centred Security', 'coordinator':'Mohamed Khamis'},
        4084: {'lec_page':lecture_page3,'course_name':'Programming and System Development', 'coordinator':'Mireilla Bikanga Ada'},
        5089: {'lec_page':lecture_page3,'course_name':'Introduction to Data Science and Systems', 'coordinator':'Nicolas Pugeault'},
        5092: {'lec_page':lecture_page3,'course_name':'Research and Professional Skills', 'coordinator':'Helen Puchase'}
    }
    course_pages2 = {
        4077: {'lec_page':lecture_page2, 'course_name':'Web Science', 'coordinator':'Joemon Jose'},
        5060: {'lec_page':lecture_page3,'course_name':'Human-Centred Security', 'coordinator':'Mohamed Khamis'},
        4084: {'lec_page':lecture_page3,'course_name':'Programming and System Development', 'coordinator':'Mireilla Bikanga Ada'},
        5089: {'lec_page':lecture_page3,'course_name':'Introduction to Data Science and Systems', 'coordinator':'Nicolas Pugeault'},
        5092: {'lec_page':lecture_page3,'course_name':'Research and Professional Skills', 'coordinator':'Helen Puchase'}
    }

    user_pages = {
        2701452:{'cos_pages':course_pages1, 'psw':'123456','email_id':'2701452J@student.gla.ac.uk', 'first_name':'Mengqi','last_name':'Jiang','gender':'Female','phone_number':1234567890},
        2701451:{'cos_pages':course_pages2, 'psw':'123456','email_id':'2701451J@student.gla.ac.uk', 'first_name':'Karen','last_name':'Jiang','gender':'Male','phone_number':1234567890}
    }


    for user, user_data in user_pages.items():
        u = add_user(user, user_data['psw'],user_data['email_id'],user_data['first_name'],user_data['last_name'],user_data['gender'],user_data['phone_number'])
        for cour, cour_data in user_data['cos_pages'].items():
            c = add_course(u,cour,cour_data['course_name'],cour_data['coordinator'])
            for lect, lect_data in cour_data['lec_page'].items():
                l = add_lecture(c, lect, lect_data['lec_name'],lect_data['url'],lect_data['content'],lect_data['length'])
                for quiz in lect_data['quiz_page']:
                    add_quiz(l,quiz['quiz_id'],quiz['question'],quiz['answer1'],quiz['answer2'],quiz['answer3'],quiz['answer4'],quiz['correct_answer'],quiz['lecture_time'])


def add_quiz(lecture,quiz_id,question,answer1,answer2,answer3,answer4,correct_answer,lecture_time):
    q = Quiz.objects.get_or_create(lecture = lecture, quiz_id = quiz_id)[0]
    q.question = question
    q.answer1 = answer1
    q.answer2 = answer2
    q.answer3 = answer3
    q.answer4 = answer4
    q.correct_answer = correct_answer
    q.lecture_time = lecture_time
    q.save()
    return q

def add_lecture(course,lec_id,lec_name,url,content,length):
    l = Lecture.objects.get_or_create(course = course,lec_id = lec_id)[0]
    l.lec_name = lec_name
    l.url = url
    l.content = content
    l.length = length
    l.save()
    return l

def add_course(user,course_id,course_name,coordinator):
    c = Course.objects.get_or_create(course_id=course_id)[0]
    c.user.add(user)
    c.course_name = course_name
    c.coordinator = coordinator
    c.save()
    return c

def add_user(user_id, psw, email_id, first_name, last_name, gender, phone_number):
    u = User.objects.get_or_create(user_id=user_id)[0]
    u.psw = psw
    u.email_id = email_id
    u.first_name = first_name
    u.last_name = last_name
    u.gender = gender
    u.phone_number = phone_number
    u.save()
    return u

if __name__ == '__main__':
    print('Starting RecQuiz population script...')
    populate()
    