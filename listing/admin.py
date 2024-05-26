from django.contrib import admin
from .models import ItemListing, VehicleListing, PropertyListing, Photo, Address


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("id", "image")


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("street_address", "city", "state", "zip_code")
    search_fields = ("street_address", "city", "state", "zip_code")


@admin.register(ItemListing)
class ItemListingAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "price",
        "status",
        "category",
        "condition",
        "location",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "status",
        "category",
        "condition",
        "location__city",
        "location__state",
    )
    search_fields = ("title", "description", "location__city", "location__state")
    filter_horizontal = ("photos",)  # Use filter_horizontal for many-to-many fields


@admin.register(VehicleListing)
class VehicleListingAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "price",
        "status",
        "type",
        "make",
        "model",
        "year",
        "mileage",
        "location",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "status",
        "type",
        "make",
        "model",
        "year",
        "location__city",
        "location__state",
    )
    search_fields = (
        "title",
        "description",
        "make",
        "model",
        "location__city",
        "location__state",
    )
    filter_horizontal = ("photos",)  # Use filter_horizontal for many-to-many fields


@admin.register(PropertyListing)
class PropertyListingAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "price",
        "status",
        "type",
        "num_bedrooms",
        "num_bathrooms",
        "square_fts",
        "date_available",
        "parking_type",
        "cat_friendly",
        "dog_friendly",
        "location",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "status",
        "type",
        "num_bedrooms",
        "num_bathrooms",
        "location__city",
        "location__state",
        "cat_friendly",
        "dog_friendly",
    )
    search_fields = ("title", "description", "location__city", "location__state")
    filter_horizontal = ("photos",)  # Use filter_horizontal for many-to-many fields
