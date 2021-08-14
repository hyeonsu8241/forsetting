from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp import views
from accountapp.views import AccountCreateView, AccountDeleteView, AccountMainView

app_name = 'accountapp'


urlpatterns = [
    path('main/', AccountMainView.as_view(), name='main'),  ### 임시 메인 페이지 경로

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', AccountCreateView.as_view(), name='create'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
    path('search/', views.search, name='search'),
]