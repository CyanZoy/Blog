from django.urls import path
from Wx import views


urlpatterns = [
    path('', views.wx_authentication),
]
