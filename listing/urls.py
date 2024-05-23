from django.urls import path
from .views import (
    ItemListingView,
    ItemListingCreateView,
    VehicleListingView,
    VehicleListingCreateView,
    PropertyListingView,
    PropertyListingCreateView,
)

urlpatterns = [
    path("item/", ItemListingView.as_view(), name="item-list"),
    path("item/create/", ItemListingCreateView.as_view(), name="item-create"),
    path("vehicle/", VehicleListingView.as_view(), name="vehicle-list"),
    path("vehicle/create/", VehicleListingCreateView.as_view(), name="vehicle-create"),
    path("property/", PropertyListingView.as_view(), name="property-list"),
    path(
        "property/create/", PropertyListingCreateView.as_view(), name="property-create"
    ),
]
