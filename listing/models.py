from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.TextChoices):
    ELECTRONICS = "EL", "Electronics"
    FURNITURE = "FU", "Furniture"
    CLOTHING = "CL", "Clothing"
    VEHICLES = "VE", "Vehicles"
    PROPERTIES = "PR", "Properties"
    BOOKS = "BK", "Books"
    SPORTS_AND_OUTDOORS = "SO", "Sports & Outdoors"
    TOYS_AND_GAMES = "TG", "Toys & Games"
    HOME_AND_GARDEN = "HG", "Home & Garden"
    SERVICES = "SV", "Services"
    OTHER = "OT", "Other"


class Condition(models.TextChoices):
    NEW = "NW", "New"
    USED = "US", "Used"
    REFURBISHED = "RF", "Refurbished"


class ListingStatus(models.TextChoices):
    AVAILABLE = "AV", "Available"
    SOLD = "SL", "Sold"


class Address(models.Model):
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.state} {self.zip_code}"


class VehicleType(models.TextChoices):
    CAR = "CR", "Car"
    TRUCK = "TR", "Truck"
    MOTORCYCLE = "MC", "Motorcycle"
    SUV = "SV", "SUV"
    VAN = "VN", "Van"
    RV = "RV", "RV"
    BOAT = "BT", "Boat"
    OTHER = "OT", "Other"


current_year = timezone.now().year
VEHICLE_YEAR_RANGE = range(current_year - 50, current_year + 1)


class VehicleYear(models.IntegerChoices):
    @classmethod
    def choices(cls):
        return [(year, str(year)) for year in VEHICLE_YEAR_RANGE]


class Photo(models.Model):
    image = models.ImageField(upload_to="listing_photos")


class BaseListingModel(models.Model):
    title = models.CharField(max_length=500)
    photos = models.ManyToManyField(
        Photo, related_name="%(app_label)s_%(class)s_related"
    )
    price = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(999999999)]
    )
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=2, choices=ListingStatus.choices, default=ListingStatus.AVAILABLE
    )
    location = models.ForeignKey(
        Address, on_delete=models.PROTECT, null=True, blank=True
    )
    views = models.PositiveIntegerField(default=0)
    favorites = models.PositiveIntegerField(default=0)
    shares = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ItemListing(BaseListingModel):
    category = models.CharField(max_length=2, choices=Category.choices)
    condition = models.CharField(max_length=2, choices=Condition.choices)


class VehicleListing(BaseListingModel):
    type = models.CharField(max_length=2, choices=VehicleType.choices)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(choices=VehicleYear.choices)
    mileage = models.PositiveIntegerField()
