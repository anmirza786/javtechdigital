from django.urls import path, include

urlpatterns = [
    path('home/', include('home.api')),
    path('services/', include('services.api')),
    path('career/', include('career.api')),
    # path('cv/', include('cv.api')),
]
