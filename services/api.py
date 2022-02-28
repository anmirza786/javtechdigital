from django.urls import path, include
from .views import (
    ProposalCreateApiView,
    PortfolioProductListApiView,
    PortfolioShowcaseListApiView
)
urlpatterns = [
    path('proposal/', ProposalCreateApiView.as_view()),
    path('portfolio/product/', PortfolioProductListApiView.as_view()),
    path('portfolio/showcase/', PortfolioShowcaseListApiView.as_view())
]
