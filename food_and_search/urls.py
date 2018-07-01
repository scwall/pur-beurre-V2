from django.urls import path, include, re_path
from food_and_search.views import DetailProduct
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index),
     path('saveproduct/', views.save_product),
    re_path(r'^result/$', views.result, name='result'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', auth_views.LogoutView.as_view()),
    path('detailproduct/<int:pk>/', DetailProduct)
]

