from django.urls import path

from commentapp.views import CommentCreateView

app_name = 'coomentapp'

urlpatterns = [
    path('',CommentCreateView.as_view(),name='create')
]