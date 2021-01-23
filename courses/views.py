from django.core.paginator import Paginator
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from courses.forms import CourseReviewForm
from courses.models import Course, Course_Curricularm, Course_Review, Category


def courses(request, category=None):

    courses = Course.objects.all()

    if category:
        courses = Course.objects.filter(category=category)

    # pagination
    paginator = Paginator(courses, 2)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)

    context = {
        'courses': paged_product,
    }


    return render(request,'courses/courses.html', context)




def courses_detail(request, slug, feature_course_slug=None, popular_course_slug=None):

    course = Course.objects.get(slug=slug)
    Welcome_To_the_courses = Course_Curricularm.objects.filter(subject='Welcome_To_the_courses').filter(course=course)
    How_to_use = Course_Curricularm.objects.filter(subject='How_to_use').filter(course=course)
    Final_chapters = Course_Curricularm.objects.filter(subject='Final_chapters').filter(course=course)

    course_review = Course_Review.objects.filter(course=course)

    feature_courses = Course.objects.filter(feature_course=True)
    categories = Category.objects.all()
    popular_courses = Course.objects.order_by('-viewers').filter(discount_price__gt=0)[:5]

# viewers will increase by 1
    Course.objects.filter(slug=slug).update(viewers=F('viewers')+1)





    if feature_course_slug:
        course = Course.objects.filter(slug=feature_course_slug)

    if popular_course_slug:
        course = Course.objects.filter(slug=popular_course_slug)

    # Course Review Form
    form = CourseReviewForm()
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('UserRegistration:login')

        form = CourseReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.course = course
            review.save()

            # messages.success(request, 'Account created successfully')
            return HttpResponseRedirect(reverse('about:about'))
    # End Course Review Form

    context = {
        'course': course,
        'Welcome_To_the_courses': Welcome_To_the_courses,
        'How_to_use': How_to_use,
        'Final_chapters': Final_chapters,
        'course_review': course_review,
        'feature_courses': feature_courses,
        'categories': categories,
        'popular_courses':popular_courses,
        'form': form,
    }

    return render(request, 'courses/courses_detail.html', context)



