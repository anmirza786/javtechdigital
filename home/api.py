from django.urls import path, include
from .views import (
    TestimonialListApiView,
    CompanyGrowthListApiView,
    OurTeamListApiView,
    ProductListApiView,
    ContactApiView
)

urlpatterns = [
    path('testimonial/', TestimonialListApiView.as_view()),
    path('growth/', CompanyGrowthListApiView.as_view()),
    path('team/', OurTeamListApiView.as_view()),
    path('products/', ProductListApiView.as_view()),
    path('contact/', ContactApiView.as_view()),
]
