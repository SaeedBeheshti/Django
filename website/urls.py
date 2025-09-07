from website.views import index_view, about_view, contact_view,Newsletter_view
from django.urls import path, URLPattern
from django.conf import settings
from django.conf.urls.static import static

app_name = 'website'

urlpatterns = [
    path('',index_view,name='index'),
    path('about',about_view, name='about'),
    path('contact',contact_view, name='contact'),
    path('newsletter',Newsletter_view, name='newsletter'),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

