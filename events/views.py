from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.

from events.models import EventModel, Category


def courses(request, event_category=None):

    events = EventModel.objects.all()

    if event_category:
        events = EventModel.objects.filter(category=event_category)



    # pagination
    paginator = Paginator(events, 2)
    page = request.GET.get('page')
    paged_event = paginator.get_page(page)

    context = {
        'events': paged_event,
    }

    return render(request,'events/events.html', context)





def event_detail(request, id):

    event = EventModel.objects.get(id=id)
    recent_events = EventModel.objects.order_by('-date')[:5]
    categories = Category.objects.all()

    context = {
        'event': event,
        'recent_events': recent_events,
        'categories': categories,
    }

    return render(request,'events/event_detail.html', context)