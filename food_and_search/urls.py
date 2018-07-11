from django.urls import path, include, re_path
from food_and_search.views import detail_product
from . import views
from django.contrib.auth import views as auth_views
app_name = 'food_and_search'
urlpatterns = [
    path('', views.index, name='index'),
    path('saveproduct/', views.save_product, name='save_product'),
    path('login/', auth_views.LoginView.as_view()),
    path('result/', views.result, name='result'),
    path('accounts/', include('django.contrib.auth.urls'),name='accounts'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/',views.signup,name='signup'),
    path('detailproduct/<int:pk>/', detail_product,name='detailproduct'),
    path('user/', views.user_account,name='user')


]

