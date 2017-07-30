from django.db.models.aggregates import Count
from django import template
from ..models import Blog, Category, Tag

register = template.Library()

# 归档模板标签
@register.simple_tag
def archives():
    return Blog.objects.dates('created', 'month', order='DESC')


# 分类模板标签
@register.simple_tag
def get_categories():
    return Category.objects.all()

# 标签云模板标签
@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('blog')).filter(num_posts__gt=0)