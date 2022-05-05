from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("details/<int:pk>", views.details , name="details"),
    path("addList/", views.listCompany, name="listCompany"),
    path("upList/<int:pk>", views.upCompany, name="upCompany"),
    path("delList/<int:pk>", views.delCompany, name="delCompany"),
    path("register/", views.signup, name="register")
]
