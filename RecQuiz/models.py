from django.db import models


class User(models.Model):
    user_id = models.IntegerField(default=0, unique=True)
    psw = models.CharField(max_length=128)
    email_id = models.CharField(max_length=128, unique=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    gender = models.CharField(max_length=128)
    phone_number = models.IntegerField(default=0)

class Course(models.Model):
    user = models.ManyToManyField(User)
    course_id = models.IntegerField(default=0, unique=True)
    coordinator = models.CharField(max_length=128)
    course_name = models.CharField(max_length=128, unique=True)


class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    url = models.CharField(max_length = 128,default="www.baidu.com")
    lec_id = models.IntegerField(default=0, unique = True)
    lec_name = models.CharField(max_length=128)
    length = models.IntegerField(default=0) 
    content = models.CharField(max_length=128)
    
class Quiz(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    quiz_id = models.IntegerField(default=0, unique=True)
    question = models.CharField(max_length=128)
    answer1 = models.CharField(max_length=128)
    answer2 = models.CharField(max_length=128)
    answer3 = models.CharField(max_length=128)
    answer4 = models.CharField(max_length=128)
    correct_answer = models.CharField(max_length=128)
    lecture_time = models.IntegerField(default = 0)







    





