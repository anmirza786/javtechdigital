from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import (
    Proposal,
    PortfolioShowcase,
    PortfolioProduct
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
