from rest_framework.serializers import ModelSerializer

from .models import (
    ItemListing,
    VehicleListing,
    PropertyListing,
    Address,
    Photo,
    Category,
    Condition,
    ListingStatus,
    VehicleType,
    VehicleYear,
    PropertyType,
    ParkingType,
)


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ["street_address", "city", "state", "zip_code"]


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ConditionSerializer(ModelSerializer):
    class Meta:
        model = Condition
        fields = "__all__"


class ListingStatusSerializer(ModelSerializer):
    class Meta:
        model = ListingStatus
        fields = "__all__"


class VehicleTypeSerializer(ModelSerializer):
    class Meta:
        model = VehicleType
        fields = "__all__"


class ItemListingSerializer(ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    location = AddressSerializer()

    class Meta:
        model = ItemListing
        fields = [
            "id",
            "title",
            "photos",
            "price",
            "description",
            "status",
            "location",
            "views",
            "favorites",
            "shares",
            "created_at",
            "updated_at",
            "category",
            "condition",
        ]

    def create(self, validated_data):
        location_data = validated_data.pop("location")
        location = Address.objects.create(**location_data)
        item_listing = ItemListing.objects.create(location=location, **validated_data)
        return item_listing


class VehicleListingSerializer(ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    location = AddressSerializer()

    class Meta:
        model = VehicleListing
        fields = [
            "id",
            "title",
            "photos",
            "price",
            "description",
            "status",
            "location",
            "views",
            "favorites",
            "shares",
            "created_at",
            "updated_at",
            "type",
            "make",
            "model",
            "year",
            "mileage",
        ]

    def create(self, validated_data):
        location_data = validated_data.pop("location")
        location = Address.objects.create(**location_data)
        vehicle_listing = VehicleListing.objects.create(
            location=location, **validated_data
        )
        return vehicle_listing


class PropertyListingSerializer(ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    location = AddressSerializer()

    class Meta:
        model = PropertyListing
        fields = [
            "id",
            "title",
            "photos",
            "price",
            "description",
            "status",
            "location",
            "views",
            "favorites",
            "shares",
            "created_at",
            "updated_at",
            "type",
            "num_bedrooms",
            "num_bathrooms",
            "square_fts",
            "date_available",
            "parking_type",
            "cat_friendly",
            "dog_friendly",
        ]

    def create(self, validated_data):
        location_data = validated_data.pop("location")
        location = Address.objects.create(**location_data)
        property_listing = PropertyListing.objects.create(
            location=location, **validated_data
        )
        return property_listing
