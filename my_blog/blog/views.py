import markdown
from django.shortcuts import render, get_object_or_404
from .models import Blog, Category, Tag
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
    post.content = markdown.markdown(post.content,
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc',
                                     ])

    return render(request, 'detail.html', {'post': post})

def home(request):
    blogs = Blog.objects.all().order_by('-created')
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
    blog_date_list = Blog.objects.filter(created__year=year, created__month=month).order_by('created')
    return render(request, 'archives.html', {'blog_date_list': blog_date_list})

def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    posts = Blog.objects.filter(category=cate).order_by('created')
    return render(request, 'category.html', {'posts': posts})

def tags(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    posts = Blog.objects.filter(tags=tag).order_by('created')
    return render(request, 'tag.html', {'posts': posts})

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