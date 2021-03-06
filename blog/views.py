from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .forms import CommentForm
from .models import Post, Category, Comment, Newsletter
from taggit.models import Tag
# from .forms import CommentForm
from django.core.paginator import Paginator
from django.db.models import Q, F


# Create your views here.


def post_list(request, news_letter=None):
    post_list = Post.objects.all()


    if news_letter:
        email = request.POST['email']
        Newsletter.objects.create(email=email)




    ## search
    search_query = request.GET.get('q')
    if search_query:
        post_list = post_list.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query) |
            Q(tags__name__icontains=search_query)
        ).distinct()

        # pagination
    paginator = Paginator(post_list, 2)
    page = request.GET.get('page')
    paged_post = paginator.get_page(page)


    context = {
        'post_list': paged_post,
    }

    return render(request, 'Post/post_list.html', context)


def post_detail(request, id):
    post_detail = Post.objects.get(id=id)
    categories = Category.objects.all()
    all_tags = Tag.objects.all()
    comments = Comment.objects.filter(post=post_detail)

    # hit will increase by 1
    Post.objects.filter(id=id).update(hit=F('hit') + 1)



# Previous and next post navigation
    widget = Post.objects.get(id=id)
    next_widget_post = Post.objects.filter(id__gt=widget.id).order_by('id').first()
    Previous_widget_post = Post.objects.filter(id__lt=widget.id).order_by('-id').first()




    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post_detail
            new_comment.save()
            print('ok')
    else:
        comment_form = CommentForm()

    context = {
        'post_detail': post_detail,
        'categories': categories,
        'all_tags': all_tags,
        'comments': comments,
        'comment_form': comment_form,
        'next_widget_post': next_widget_post,
        'Previous_widget_post': Previous_widget_post,
    }

    return render(request, 'Post/post_detail.html', context)


def post_by_tag(request, tag):
    post_by_tag = Post.objects.filter(tags__name__in=[tag])
    context = {
        'post_list': post_by_tag,
    }

    return render(request, 'Post/post_list.html', context)


def post_by_category(request, category):
    post_by_category = Post.objects.filter(category__slug=category)
    context = {
        'post_list': post_by_category,
    }

    return render(request, 'Post/post_list.html', context)


def news_letter(request):
    if request.method == "POST":
        email = request.POST['email']

        Newsletter.objects.create(email=email)






