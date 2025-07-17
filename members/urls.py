from django.urls import path
from . import views

urlpatterns = [
    path("all_members/", views.members, name="all_members"),
    path("all_members/details/<int:id>", views.details, name="details"),
]
