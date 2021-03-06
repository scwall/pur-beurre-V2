from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic import TemplateView

from food_and_search.views import detail_product
from . import views
# Application urls route
app_name = 'food_and_search'
urlpatterns = [
    path('', views.index, name='index'),
    path('saveproduct/', views.save_product, name='save_product'),
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html"), {'next_page': '/'}, name='login'),
    path('result/', views.result, name='result'),
    path('accounts/', include('django.contrib.auth.urls'), name='accounts'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('detailproduct/<int:pk>/', detail_product, name='detailproduct'),
    path('user/', views.user_account, name='user'),
    path('mention-legale/', TemplateView.as_view(template_name='legal_notice.html'), name='legalnotice')
]
