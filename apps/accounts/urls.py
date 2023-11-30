from django.urls import path

from apps.accounts.views import index

urlpatterns = [
    path('', index),
]