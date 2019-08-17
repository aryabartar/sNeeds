"""Ticket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

app_name = "tweets"

urlpatterns = [
    # path('tweets/', views.TweetListAPIView.as_view()),
    # # path('<int:personId>/', CreateRetrieveMessageAPIView.as_view()),
    # path('tweets/<int:id>/', views.TweetDetailAPIView.as_view(), name="tweet-detail"),


    path('tickets/', views.TweetListAPIView.as_view()),
    path('tickets/<int:id>/', views.TweetDetailAPIView.as_view(), name="tweet-detail"),
    path('tickets/<int:id>/messages/', views.TweetDetailAPIView.as_view(), name="tweet-detail"),
    path('tickets/<int:id>/messages/<int:id>/', views.TweetDetailAPIView.as_view(), name="tweet-detail"),
]
