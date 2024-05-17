from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import MarketplaceUser


class MarketplaceUserAdmin(UserAdmin):
    list_display = ("email", "phone_number", "first_name", "last_name", "is_admin")
    list_filter = ("is_admin",)
    search_fields = ("email", "phone_number")
    ordering = ("email",)
    filter_horizontal = ()
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "phone_number",
                    "first_name",
                    "last_name",
                    "password",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_admin",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Personal info", {"fields": ("profile_picture", "whatsapp_number")}),
        ("Important dates", {"fields": ("created_at", "updated_at")}),
    )


admin.site.register(MarketplaceUser, MarketplaceUserAdmin)
