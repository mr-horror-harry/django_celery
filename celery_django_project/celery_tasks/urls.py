from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add_req, name="add"),
    path('sub', views.sub_req, name="sub"),
    path('mul', views.mul_req, name="mul"),
]
