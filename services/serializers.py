from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import (
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


class ServiceSerializer(serializers.ModelField):
    class Meta:
        model = Services
        fields = '__all__'


class ServicesSerializer(serializers.ModelSerializer):
    # language = Services(many=True, read_only=True)
    # print(course)

    class Meta:
        model = Services
        fields = [
            'id',
            'category',
            'title',
            'description',
            'slug',
        ]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
