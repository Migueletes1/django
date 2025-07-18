from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("all_members/", views.members, name="all_members"),
    path("all_members/details/<int:id>", views.details, name="details"),
    path("testing/", views.testing, name="testing"),
]
