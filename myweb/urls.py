from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('blog/', views.blog, name='blog-detail'),
    path('projects/', views.projects, name='blog-projects'),
]
