from django.contrib import admin
from django.contrib.auth import models as base_models
from django.contrib.auth.admin import UserAdmin as CoreUserAdmin

from . import models


@admin.register(models.User)
class UserAdmin(CoreUserAdmin):
    ordering = ["id"]
    list_display = (
        "id",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_superuser",
        "last_login",
        "date_joined",
    )
    list_display_links = ("id", "email")
    list_filter = ("is_active", "is_staff", "is_superuser", "last_login", "date_joined")
    search_fields = ("email", "first_name", "last_name",)

    fieldsets = (
        (None, {"fields": ("password",)}),
        ("Information", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = ((None, {"fields": ["email", "first_name", "last_name", "password1", "password2"]}),)


admin.site.unregister(base_models.Group)


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
