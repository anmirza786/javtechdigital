from django.urls import path
from .views import (
    CourseFormCreateApiView,
    IntershipFormCreateApiView
)
urlpatterns = [
    path('course/', CourseFormCreateApiView.as_view()),
    path('internship/', IntershipFormCreateApiView.as_view()),
]
