from django.contrib import admin
from django.urls import path
# from sso.views import register_1,login_1,logout_1,home_1,activate
from . import views

urlpatterns = [
    path('register',views.register_1,name='register'),
    path('login',views.login_1,name='login'),
    path('logout',views.logout_1,name='logout'),
    path('home',views.home_1,name= 'home'),
    path('activate/<int:pk>',views.activate,name= 'activate'),
    # path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',views.activate,name='activate'),  


]
