from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from .models import ItemListing, VehicleListing, PropertyListing, Photo
from .serializers import (
    ItemListingSerializer,
    VehicleListingSerializer,
    PropertyListingSerializer,
)


class ItemListingView(APIView):

    def get(self, request):
        item_listings = ItemListing.objects.select_related("location").prefetch_related(
            "photos"
        )
        serializer = ItemListingSerializer(item_listings, many=True)
        return Response(serializer.data)


class ItemListingCreateView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        serializer = ItemListingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class VehicleListingView(APIView):

    def get(self, request):
        vehicle_listings = VehicleListing.objects.select_related(
            "location"
        ).prefetch_related("photos")
        serializer = VehicleListingSerializer(vehicle_listings, many=True)
        return Response(serializer.data)


class VehicleListingCreateView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        serializer = VehicleListingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PropertyListingView(APIView):

    def get(self, request):
        property_listings = PropertyListing.objects.select_related(
            "location"
        ).prefetch_related("photos")
        serializer = PropertyListingSerializer(property_listings, many=True)
        return Response(serializer.data)


class PropertyListingCreateView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        serializer = PropertyListingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
