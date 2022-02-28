from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .serializers import (
    TestimonialSerializer,
    CompanyGrowthSerializer,
    OurTeamSerializer,
    ProductSerializer,
    ContactSerializer
)
from rest_framework.response import Response
from rest_framework import permissions
from .models import (
    Testimonial,
    CompanyGrowth,
    OurTeam,
    Product,
    Contact,
)
# Create your views here.


class TestimonialListApiView(ListAPIView):
    permision_classes = (permissions.AllowAny,)
    serializer_class = TestimonialSerializer

    def get_queryset(self):
        return Testimonial.objects.filter(
            home_display=True).order_by('-id')


class CompanyGrowthListApiView(ListAPIView):
    permision_classes = (permissions.AllowAny,)
    serializer_class = CompanyGrowthSerializer

    def get_queryset(self):
        return CompanyGrowth.objects.all()


class OurTeamListApiView(ListAPIView):
    permision_classes = (permissions.AllowAny,)
    serializer_class = OurTeamSerializer

    def get_queryset(self):
        return OurTeam.objects.all().order_by('-id')


class ProductListApiView(ListAPIView):
    permision_classes = (permissions.AllowAny,)
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('-id')


class ContactApiView(APIView):
    serializer_class = ContactSerializer
    # permision_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        try:
            Contact.objects.create(
                email=request.data['email'], message=request.data['message'])
            return Response({'success': 'Your message is submitted'})
        except Exception as e:
            Response({'error':'e'})
