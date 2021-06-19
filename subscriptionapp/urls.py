from django.urls import path

from subscriptionapp.views import SubscribeView, SubscribeListView

app_name = 'subscriptionapp'

urlpatterns = [
    path('',SubscribeView.as_view(),name='subscribe'),
    path('list/',SubscribeListView.as_view(),name='list')
]