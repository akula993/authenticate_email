from django.urls import path, include
from django.views.generic import TemplateView

from users.views import Register

urlpatterns = [

    path('', TemplateView.as_view(template_name='device/home.html'), name='device'),
]
