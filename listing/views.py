from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status, filters
from .models import ItemListing, VehicleListing, PropertyListing, Photo
from .serializers import (
    ItemListingSerializer,
    VehicleListingSerializer,
    PropertyListingSerializer,
)
from django.db.models import Q


class ItemListingAPIView(ListCreateAPIView):
    queryset = ItemListing.objects.select_related("location").prefetch_related("photos")
    serializer_class = ItemListingSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        "title",
        "description",
        "category",
        "location__city",
        "location__state",
    ]
    ordering_fields = ["price", "created_at", "views", "favorites"]


class VehicleListingAPIView(ListCreateAPIView):
    queryset = VehicleListing.objects.select_related("location").prefetch_related(
        "photos"
    )
    serializer_class = VehicleListingSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        "title",
        "description",
        "make",
        "model",
        "type",
        "location__city",
        "location__state",
    ]
    ordering_fields = ["price", "created_at", "views", "favorites"]


class PropertyListingAPIView(ListCreateAPIView):
    queryset = PropertyListing.objects.select_related("location").prefetch_related(
        "photos"
    )
    serializer_class = PropertyListingSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        "title",
        "description",
        "type",
        "location__city",
        "location__state",
    ]
    ordering_fields = ["price", "created_at", "views", "favorites"]


class ItemListingDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ItemListing.objects.select_related("location").prefetch_related("photos")
    serializer_class = ItemListingSerializer


class VehicleListingDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = VehicleListing.objects.select_related("location").prefetch_related(
        "photos"
    )
    serializer_class = VehicleListingSerializer


class PropertyListingDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = PropertyListing.objects.select_related("location").prefetch_related(
        "photos"
    )
    serializer_class = PropertyListingSerializer
