from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,),
    path('signup/', views.signup_view,),
    path('login/', views.login, ),
    path('user/', views.userpage)
]