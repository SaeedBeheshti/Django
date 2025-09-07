from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from website.forms import NameForm,ContactForm


def blog_view(request):
    posts_list = Post.objects.filter(status=1)
    paginator = Paginator(posts_list, 3)  # 3 پست در هر صفحه
    page_number = request.GET.get('page')  # گرفتن شماره صفحه از URL

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # اگر شماره صفحه عدد نبود، صفحه اول نمایش داده شود
        posts = paginator.page(1)
    except EmptyPage:
        # اگر شماره صفحه بزرگتر از تعداد صفحات بود، آخرین صفحه نمایش داده شود
        posts = paginator.page(paginator.num_pages)

    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    post = get_object_or_404(Post, pk=pid, status=1)
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)


from django.shortcuts import render
from django.http import HttpResponse
from website.forms import NameForm

def test(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')
    else:  # GET
        form = ContactForm()  # فرم خالی ساخته میشه

    return render(request, 'blog/test.html', {'form': form})
