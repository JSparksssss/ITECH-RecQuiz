from django.db import models
from django.template.defaultfilters import slugify

class User(models.Model):
    user_id = models.IntegerField(default=0, unique=True)
    psw = models.CharField(max_length=128)
    email_id = models.CharField(max_length=128, unique=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    gender = models.CharField(max_length=128)
    phone_number = models.IntegerField(default=0)
    slug = models.SlugField(blank=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.user_id)
        super(User,self).save(*args, **kwargs)

class Course(models.Model):
    user = models.ManyToManyField(User)
    course_id = models.IntegerField(default=0, unique=True)
    coordinator = models.CharField(max_length=128)
    course_name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.course_name)
        super(User,self).save(*args, **kwargs)


class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lec_id = models.IntegerField(default=0, unique = True)
    lec_name = models.CharField(max_length=128)
    length = models.IntegerField(default=0)
    content = models.CharField(max_length=128)
    time = models.IntegerField(default=0)
    
class Quiz(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    quiz_id = models.IntegerField(default=0, unique=True)
    quiz_name = models.CharField(max_length=128)
    question = models.CharField(max_length=128)
    answer = models.CharField(max_length=128)
    correct_answer = models.CharField(max_length=128)
    lecture_time = models.IntegerField(default = 0)







    





