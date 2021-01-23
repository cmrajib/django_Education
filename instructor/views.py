from django.shortcuts import render

# Create your views here.
from courses.models import Course
from instructor.models import Instructor, Skill


def profile(request, id):
    instructor = Instructor.objects.get(id=id)
    courses = Course.objects.filter(instructor=id)
    skills = Skill.objects.filter(instructor=id)

    context = {
        'instructor': instructor,
        'courses': courses,
        'skills': skills,
    }

    return render(request,'instructor/profile.html', context)