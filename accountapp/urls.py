from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include, reverse_lazy

from accountapp.views import home, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = 'accountapp'

urlpatterns = [
    path('',home,name='home'),
    path('login/',LoginView.as_view(template_name='accountapp/login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('create/',AccountCreateView.as_view(),name='create'),
    path('mypage/<int:pk>',AccountDetailView.as_view(),name='detail'),
    path('change/<int:pk>',AccountUpdateView.as_view(),name='update'),
    path('quit/<int:pk>',AccountDeleteView.as_view(),name='delete'),
]
