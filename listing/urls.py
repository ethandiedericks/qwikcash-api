from django.urls import path
from .views import (
    ItemListingListView,
    ItemListingListCreateAPIView,
    ItemListingDetailAPIView,
    VehicleListingListView,
    PropertyListingListView,
)

urlpatterns = [
    path("items/", ItemListingListView.as_view(), name="item-list"),
    path("items/create/", ItemListingListCreateAPIView.as_view(), name="item-create"),
    path("items/<int:pk>/", ItemListingDetailAPIView.as_view(), name="item-detail"),
    path("vehicles/", VehicleListingListView.as_view(), name="vehicle-list"),
    path("properties/", PropertyListingListView.as_view(), name="property-list"),
]
