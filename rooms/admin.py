from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.
@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    list_display = ("name", "used_by")

    """ Item Admin Definition """

    def used_by(self, obj):
        return obj.rooms.count()

    pass


class PhotoInline(admin.TabularInline):

    model = models.photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "city", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        ("Last Details", {"fields": ("host",)},),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "host__gender",
        "room_type",
        "city",
        "country",
    )

    raw_id_fields = ("host",)

    search_fields = ("=city", "^host__username")

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    def count_amenities(self, obj):
        return obj.amenities.count()

    count_amenities.short_description = "Amenities"

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photos Count"


@admin.register(models.photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"