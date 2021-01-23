from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from contact.forms import ContactForm
from courses.models import Instructor


def about(request):

    Instructors = Instructor.objects.all()

    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Account created successfully')
            return HttpResponseRedirect(reverse('about:about'))


    context = {
        'Instructors': Instructors,
        'form': form,
    }

    return render(request,'about/about.html', context)