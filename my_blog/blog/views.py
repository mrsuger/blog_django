from django.shortcuts import render
from .models import Blog, Category
from .forms import CommentForm
from django.http import Http404, HttpResponse
# 导入分页包
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def detail(request, blog_id):
    try:
        post = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404

    return render(request, 'detail.html', {'post': post})

def home(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    try:
        blog_post = paginator.page(page)
    except PageNotAnInteger:
        blog_post = paginator.page(1)
    except EmptyPage:
        blog_post = paginator.paginator(paginator.num_pages)
    return render(request, 'home.html', {'blog_post': blog_post})

def about_me(request):
    return render(request,'aboutme.html')

# archives页面获得year和month参数，从而显示相应的页面
def archives(request, year, month):
    blog_date_list = Blog.objects.filter(created__year=year, created__month=month)
    return render(request, 'archives.html', {'blog_date_list': blog_date_list})

def category(request, category_name):
    posts = Blog.objects.filter(category=category_name)
    return render(request, 'category.html', {'posts': posts})

def search(request):
    # s为表单输入的参数
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, 'home.html')
        else:
            post_list = Blog.objects.filter(title__icontains = s)
            if len(post_list) == 0:
                return render(request, 'search.html', {'post_list': post_list,
                                                       'error': True})
            else:
                return render(request, 'search.html', {'post_list': post_list,
                                                       'error': False})
    return redirect('/')