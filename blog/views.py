
from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Post, Category, Tag
from comments.forms import CommentForm
import markdown

# Create your views here.

# 类视图，继承 ListView
class IndexView(ListView):

    # 指定要获取数据的模型
    model = Post
    # 指定渲染的页面
    template_name = 'blog/index.html'
    # 指定获取模型列表数据保存的变量名
    context_object_name = 'post_list'

def index(request):

    post_list = Post.objects.all()

    return render(request, 'blog/index.html', context={'post_list' : post_list})



def about(request):
    return render(request, 'blog/about.html')

def fullwidth(request):
    return render(request, 'blog/fullwidth.html')

def contact(request):
    return render(request, 'blog/contact.html')


def detail(request, pk):
    #从数据库查Post表的，无结果报404
    post = get_object_or_404(Post, pk=pk)

    # 阅读量 +1
    post.increase_views()

    post.body = markdown.markdown(post.body,extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc'])
    form = CommentForm()
    #获取 post 下面的评论
    comment_list = post.comment_set.all()

    #将数据交给 detail.html 模板，渲染
    context = {'post' : post,
               'form' : form,
               'comment_list' : comment_list}
    return render(request, 'blog/detail.html', context=context)



def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month,
                                    )
    return render(request, 'blog/index.html', context={'post_list' : post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request, 'blog/index.html', context={'post_list' : post_list})


def tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tag=tag)
    return render(request, 'blog/index.html', context={'post_list' : post_list})