from django.urls import path

from . import views

app_name = "payment"

urlpatterns = [
    path('request/', views.SendRequest.as_view(), name='request'),
    path('verify/', views.verify, name='verify'),
]