from django.urls import path, include, re_path

from . import views

urlpatterns = [
    path('', views.index),
    # path('signup/', views.signup_view,),
    # path('login/', views.login, ),
     path('user/', views.userpage),
    re_path(r'^result/$', views.result, name='result'),
]

