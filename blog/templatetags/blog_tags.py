from django import template
from ..models import Post, Category, Tag

register = template.Library()  # 实例化 template.Library 类

@register.simple_tag  #注册为模板标签，以便使用语法{% get_recent_posts %}调用
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')
    #根据dates返回一个列表

@register.simple_tag
def get_categories():
    return Category.objects.all()

@register.simple_tag
def get_tag():
    return Tag.objects.all()