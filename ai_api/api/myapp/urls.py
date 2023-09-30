from django.urls import path
from . import views

urlpatterns = [
    path('get-questionare', views.get_questionaire, name="get_questionare"),
]


