from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Photo(models.Model):
    image = models.ImageField(upload_to="listing_photos")


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Condition(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BaseListingModel(models.Model):
    photos = models.ManyToManyField(
        Photo, related_name="%(app_label)s_%(class)s_related"
    )
    price = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(999999999)]
    )
    phone_number = models.CharField(max_length=20)
    whatsapp_number = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ItemListing(BaseListingModel):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    condition = models.ForeignKey(Condition, on_delete=models.PROTECT)


class VehicleListing(BaseListingModel):
    title = models.CharField(max_length=200)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField()


class PropertyListing(BaseListingModel):
    title = models.CharField(max_length=200)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    num_bedrooms = models.PositiveIntegerField()
    num_bathrooms = models.PositiveIntegerField()
