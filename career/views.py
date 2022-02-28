from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework import permissions, serializers
from rest_framework.response import Response
from .serializers import(
    CourseFormSerializer,
    IntershipFormSerializer
)
from .models import(
    CourseForm,
    InternshipForm
)


class CourseFormCreateApiView(CreateAPIView):
    permision_classes = (permissions.AllowAny)
    serializer_class = CourseFormSerializer

    def post(self, request, *args, **kwargs):
        data = self.request.data
        CourseForm.objects.create(
            firstname=data['firstname'],
            lastname=data['lastname'],
            email=data['email'],
            phone=data['phone'],
            course=data['course']
        )
        return Response({'success': "Thanks for submiting Course form. Our team will contact to you soon."})


class IntershipFormCreateApiView(CreateAPIView):
    permision_classes = (permissions.AllowAny)
    serializer_class = IntershipFormSerializer

    def post(self, request, *args, **kwargs):
        data = self.request.data
        InternshipForm.objects.create(
            firstname=data['firstname'],
            lastname=data['lastname'],
            email=data['email'],
            phone=data['phone'],
            cv=data['cv']
        )
        return Response({'success': "Thanks for Submiting intership form. Our team will contact to you soon."})
