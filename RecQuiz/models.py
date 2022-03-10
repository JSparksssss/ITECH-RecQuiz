from django.db import models
from django.template.defaultfilters import slugify

class User(models.Model):
    user_id = models.IntegerField(default=0)
    psw = models.CharField(max_length=128)
    email_id = models.CharField(max_length=128)
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
    course_id = models.IntegerField(default=0)
    coordinator = models.CharField(max_length=128)
    course_name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.course_name)
        super(Course,self).save(*args, **kwargs)

class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    url = models.CharField(max_length = 128,default="www.baidu.com")
    lec_id = models.IntegerField(default=0)
    lec_name = models.CharField(max_length=128)
    length = models.IntegerField(default=0) 
    content = models.CharField(max_length=128)
    
class Quiz(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    quiz_id = models.IntegerField(default=0)
    question = models.CharField(max_length=128)
    answer1 = models.CharField(max_length=128)
    answer2 = models.CharField(max_length=128)
    answer3 = models.CharField(max_length=128)
    answer4 = models.CharField(max_length=128)
    correct_answer = models.CharField(max_length=128)
    lecture_time = models.IntegerField(default = 0)

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The additional attributes we wish to include.
    phone = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    # picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user





    





