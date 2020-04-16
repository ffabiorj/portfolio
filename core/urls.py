from django.urls import path
from core import views as view

urlpatterns = [
    path("", view.home, name="home")
]
