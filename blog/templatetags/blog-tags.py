from django import template
from blog.models import Post
register = template.Library()

@register.simple_tag(name='totalposts')
def function():
    post = Post.objects.filter(status=1).count()
    return post
@register.filter
def snipped(value):
    return value[:100]
@register.inclusion_tag('blog/popular-posts.html')
def latestsposts():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:1]
    return {'posts':posts}
