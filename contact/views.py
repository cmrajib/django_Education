from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from contact.forms import ContactForm


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Account created successfully')
            return HttpResponseRedirect(reverse('home:home'))
    return render(request,'contact/contact.html', {'form': form})

