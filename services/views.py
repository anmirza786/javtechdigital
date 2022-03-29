from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework import permissions
from rest_framework.response import Response
from .serializers import (
    CategorySerializer,
    ProposalSerializer,
    PortfolioProductSerializer,
    PortfolioShowcaseSerializer,
    ServiceSerializer,
)
from .models import (
    Category,
    Proposal,
    PortfolioProduct,
    PortfolioShowcase,
    Services
)


class ProposalCreateApiView(CreateAPIView):
    permision_classes = (permissions.AllowAny,)
    serializer_class = ProposalSerializer

    def post(self, request, *args, **kwargs):
        data = self.request.data
        Proposal.objects.create(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            proposalText=data['proposalText']
        )
        return Response({'success': "Thanks for contacting us. Our team will contact to you soon."})


class PortfolioProductListApiView(ListAPIView):
    permision_classes = (permissions.AllowAny,)
    serializer_class = PortfolioProductSerializer

    def get_queryset(self):
        return PortfolioProduct.objects.all()


class PortfolioShowcaseListApiView(ListAPIView):
    permision_classes = (permissions.AllowAny,)
    serializer_class = PortfolioShowcaseSerializer

    def get_queryset(self):
        return PortfolioShowcase.objects.all()


class ServiceListApiView(ListAPIView):
    permision_classes = (permissions.AllowAny,)
    serializer_class = ServiceSerializer
    # http_method_names = ['get']

    def get_queryset(self):
        return Services.objects.all()

# class


class CategoryListApiView(ListAPIView):
    permision_classes = (permissions.AllowAny,)
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()
