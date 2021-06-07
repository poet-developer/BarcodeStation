from django.urls import path

from profileapp.views import ProfileCreateView

app_name = 'profileapp'

urlpatterns = [
    path('',ProfileCreateView.as_view(),name='create')
]