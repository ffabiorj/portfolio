from django.urls import path
from blog import views as view

urlpatterns = [
    path('', view.blogs, name='blogs'),
    path('<int:pk>/', view.blog_detail, name='blog_detail'),
    path('<category>', view.blog_category, name='blog_category'),
]
