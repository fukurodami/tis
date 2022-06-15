from unicodedata import name
from django.urls import path, include
from wash import views

urlpatterns = [
    path("", views.CatalogView.as_view()),
    path("<int:pk>/", views.PostView.as_view()),
    path("us/", views.UsView.as_view()),
]