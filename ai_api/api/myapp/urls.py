from django.urls import path
from . import views

urlpatterns = [
    path('get', views.get_data, name="get_data"),
    path('post', views.post_data, name="post_data")
]


