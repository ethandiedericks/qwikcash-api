from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import ItemListing, VehicleListing, PropertyListing, Photo
from .serializers import (
    ItemListingSerializer,
    VehicleListingSerializer,
    PropertyListingSerializer,
)


class ItemListingListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        item_listings = ItemListing.objects.select_related("location").prefetch_related(
            "photos"
        )
        serializer = ItemListingSerializer(item_listings, many=True)
        return Response(serializer.data)


class VehicleListingListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        vehicle_listings = VehicleListing.objects.select_related(
            "location"
        ).prefetch_related("photos")
        serializer = VehicleListingSerializer(vehicle_listings, many=True)
        return Response(serializer.data)


class PropertyListingListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        property_listings = PropertyListing.objects.select_related(
            "location"
        ).prefetch_related("photos")
        serializer = PropertyListingSerializer(property_listings, many=True)
        return Response(serializer.data)


class ItemListingListCreateAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        item_listings = ItemListing.objects.select_related("location").prefetch_related(
            "photos"
        )
        serializer = ItemListingSerializer(item_listings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItemListingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemListingDetailAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return ItemListing.objects.get(pk=pk)
        except ItemListing.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        item_listing = self.get_object(pk)

        if not item_listing:
            return Response(
                {"message": "Item does not exist"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = ItemListingSerializer(item_listing)
        return Response(serializer.data)

    def put(self, request, pk):
        item_listing = self.get_object(pk)

        if not item_listing:
            return Response(
                {"message": "Item does not exist"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = ItemListingSerializer(item_listing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        item_listing = self.get_object(pk)

        if not item_listing:
            return Response(
                {"message": "Item does not exist"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = ItemListingSerializer(
            item_listing, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        item_listing = self.get_object(pk)

        if not item_listing:
            return Response(
                {"message": "Item does not exist"}, status=status.HTTP_404_NOT_FOUND
            )

        item_listing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
