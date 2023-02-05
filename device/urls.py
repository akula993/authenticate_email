from django.urls import path, include
from django.views.generic import TemplateView

from device.views import HomeListView
from users.views import Register

urlpatterns = [

    path('', HomeListView.as_view(), name='device'),
]
