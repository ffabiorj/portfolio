from django.urls import path
from blog import views as view

urlspatters = [
    path('', view.blogs, name='blogs'),
]
