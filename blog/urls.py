from blog.views import blog_view, blog_single, test
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='index'),
    path('post-<int:pid>/', blog_single, name='single'),
    path('test' , test, name='test'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
