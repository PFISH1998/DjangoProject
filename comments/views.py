from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post

from .models import Comment
from .forms import CommentForm


def post_comment(request, pk):
    print(pk)
    post = get_object_or_404(Post, pk=pk)
    # 获取文章评论，得到评论文章的pk

    if request.method == 'POST':
        # 当用户请求为 pos t时处理表单数据

        # 构造成 CommentForm 的实例
        form = CommentForm(request.POST)

        # 检查表单是否符合格式要求
        if form.is_valid():

            # 调用save方法保存到数据库
            # commit=False 的作用是利用表单生成 Commment 模型类的实例，不保存数据
            comment = form.save(commit=False)

            # 将评论数据与被评论的文章关联起来
            comment.post = post

            # 最终保存
            comment.save()
            # 重定向到 post 页
            return redirect(post)

        else:
            # 数据不合法重新渲染
            comment_list = post.comment_set.all()
            context = {'post' : post,
                       'form' : form,
                       'comment_list' : comment_list
                       }
            return render(request, 'blog/detail.html', context=context)

    # 重定向到 post 页
    return redirect (post)
