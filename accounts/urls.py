from django.urls import path
from .views import login_view, signup_view


app_name = 'accounts'

urlpatterns = [
    #   log in
    path('login',login_view,name='login'),
    #   log out
  #  path('logout',logout_view,name='logout'),
    #   Registration/sign up
    path('signup',signup_view,name='signup'),


]