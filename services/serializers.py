from asyncore import read
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import (
    Category,
    Proposal,
    PortfolioShowcase,
    PortfolioProduct,
    Services
)


class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = '__all__'


class PortfolioShowcaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioShowcase
        fields = '__all__'


class PortfolioProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioProduct
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    services = ServiceSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = [
            'category',
            'category_description',
            'services'
        ]
