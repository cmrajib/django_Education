from django.shortcuts import render

# Create your views here.
from courses.models import Course
from events.models import EventModel


def home(request):

    popular_courses = Course.objects.order_by('-viewers')
    events = EventModel.objects.order_by('-datetime')

    context = {
        'popular_courses': popular_courses,
        'events': events,
    }

    return render(request,'home/home.html', context)