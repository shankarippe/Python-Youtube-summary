from django.urls import path
from . import views

urlpatterns = [
    path('', views.summarize_view, name='summarize'),
]
