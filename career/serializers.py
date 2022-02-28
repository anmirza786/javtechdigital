from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import (
    CourseForm,
    InternshipForm
)


class CourseFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseForm
        fields = '__all__'


class IntershipFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternshipForm
        fields = '__all__'
