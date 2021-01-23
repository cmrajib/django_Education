from django.db import models

# Create your models here.
from UserRegistration.models import User
from instructor.models import Instructor


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def course_count(self):
        return self.categories.all().count()

class Course(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    image = models.ImageField(upload_to='course', default='no-name.jpg', null=True)
    price = models.IntegerField(default=0, blank=True)
    discount_price = models.IntegerField(default=0, blank=True)


    instructor = models.ManyToManyField(Instructor)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    no_of_students = models.IntegerField(default=0)
    lessons = models.CharField(max_length=100)
    viewers = models.IntegerField(default=0)
    duration = models.CharField(max_length=100)

    feature_course = models.BooleanField(default=False)

    prequisite = models.CharField(max_length=100)
    certificate = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    assessments = models.CharField(max_length=100)

    course_description = models.TextField()
    what_will_i_learn = models.TextField()
    learning_outcomes = models.TextField()

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name

    # instructor_names is displayed in list_display in admin.py
    def instructor_names(self):
        return ', '.join([a.name for a in self.instructor.all()])

    instructor_names.short_description = "Instructor Names"
    # instructor_names is displayed in list_display in admin.py


class Course_Curricularm(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE, related_name='course_curricularm')
    lecture = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

    user_choice= (
        ('Welcome_To_the_courses','Welcome To the courses'),
        ('How_to_use', 'How to use'),
        ('Final_chapters', 'Final chapters'),
    )

    subject=models.CharField(max_length=50, choices=user_choice)

    class Meta:
        verbose_name = 'Course_Curricularm'
        verbose_name_plural = 'Course_Curricularm'

    def __str__(self):
        return self.course.name

class Course_Review(models.Model):
    user_choice = (
        ('11111', '5'),
        ('1111', '4'),
        ('111', '3'),
        ('11', '2'),
        ('1', '1'),
    )
    course = models.ForeignKey(Course,on_delete=models.CASCADE, related_name='course_review')
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='course_review_user')
    rating = models.CharField(max_length=10,choices=user_choice,  default=0)
    comments = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Course_Review'
        verbose_name_plural = 'Course_Review'

    def __str__(self):
        return self.course.name



