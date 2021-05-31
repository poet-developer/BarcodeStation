from django.urls import path, include

from accountapp.views import home

app_name = 'accountapp'

urlpatterns = [
    path('',home,name='home')
]
