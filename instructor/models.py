from django.db import models

# Create your models here.
from UserRegistration.models import User

class Department(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField()

    def __str__(self):
        return self.name

class Instructor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='Instructor')
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    image = models.ImageField(upload_to='Instructor', default='no-name.jpg', null=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='department')
    Experience = models.CharField(max_length=30)
    Language = models.CharField(max_length=30)

    About_Instructor = models.TextField()
    Qualification = models.TextField()

    class Meta:
        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructors'

    def __str__(self):
        return self.name



class Skill(models.Model):
    instructor = models.ForeignKey(Instructor,on_delete=models.CASCADE, related_name='Instructor')
    name = models.CharField(max_length=30)
    percentage = models.IntegerField(default=0)

    def __str__(self):
        return self.instructor.name +' - ' + self.name