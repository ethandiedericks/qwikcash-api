from django.urls import path
from .views import (
    ItemListingAPIView,
    VehicleListingAPIView,
    PropertyListingAPIView,
    ItemListingDetailAPIView,
    VehicleListingDetailAPIView,
    PropertyListingDetailAPIView,
)

urlpatterns = [
    path("item/", ItemListingAPIView.as_view(), name="item-list"),
    path("item/<int:pk>/", ItemListingDetailAPIView.as_view(), name="item-detail"),
    path("vehicle/", VehicleListingAPIView.as_view(), name="vehicle-list"),
    path(
        "vehicle/<int:pk>/",
        VehicleListingDetailAPIView.as_view(),
        name="vehicle-detail",
    ),
    path("property/", PropertyListingAPIView.as_view(), name="property-list"),
    path(
        "property/<int:pk>/",
        PropertyListingDetailAPIView.as_view(),
        name="property-detail",
    ),
]
