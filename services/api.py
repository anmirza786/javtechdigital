from django.urls import path, include
from .views import (
    CategoryListApiView,
    ProposalCreateApiView,
    PortfolioProductListApiView,
    PortfolioShowcaseListApiView,
    ServiceListApiView
)
urlpatterns = [
    path('', ServiceListApiView.as_view()),
    path('proposal/', ProposalCreateApiView.as_view()),
    path('portfolio/product/', PortfolioProductListApiView.as_view()),
    path('portfolio/showcase/', PortfolioShowcaseListApiView.as_view()),
    path('portfolio/showcase/', PortfolioShowcaseListApiView.as_view()),
    path('portfolio/showcase/', PortfolioShowcaseListApiView.as_view()),
    path('service/', ServiceListApiView.as_view()),
    path('category/', CategoryListApiView.as_view()),
]
