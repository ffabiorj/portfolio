from django.urls import path
from core import views as view

urlpatterns = [
    path("", view.home, name="home"),
    path("project/<int:pk>/", view.project_detail, name="project_detail")
]
