from rest_framework import serializers
from .models import (
    Testimonial,
    CompanyGrowth,
    OurTeam,
    Product,
    Contact
)


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'


class CompanyGrowthSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyGrowth
        fields = '__all__'


class OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeam
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
