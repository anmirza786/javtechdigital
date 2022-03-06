from django.urls import path, include
from .views import (
    ProposalCreateApiView,
    PortfolioProductListApiView,
    PortfolioShowcaseListApiView,
    ServicesListApiView,
    ServiceListApiView
)
urlpatterns = [
    path('', ServiceListApiView.as_view()),
    path('proposal/', ProposalCreateApiView.as_view()),
    path('portfolio/product/', PortfolioProductListApiView.as_view()),
    path('portfolio/showcase/', PortfolioShowcaseListApiView.as_view()),
    path('portfolio/showcase/', PortfolioShowcaseListApiView.as_view()),
    path('portfolio/showcase/', PortfolioShowcaseListApiView.as_view()),
    path('<slug:slug>/', ServicesListApiView.as_view()),
]
