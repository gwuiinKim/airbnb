from django.contrib import admin
from . import models




@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    
    """ Item Admin Definition """
    
    list_display = ("name", "used_by")
    
    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ """
    pass
    
@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    
    """Room Admin Definition"""
    
    fieldsets = (
        (
            "Basic Info", 
            {
                "fields" : 
                ("name", "description", "country", "address", "price",)
            }
        ),
        (
            "More About the Space",
            {
                "classes" : ("collapse"),
                "fields" : 
                ("amenities", "facilities", "house_rules",)
            }
        )
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
    
    #can access through foreignkey by using __
    list_filter = (
        "host__superhost",
        "instant_book", 
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city", 
        "country",
    )

    search_fields = ("=city", "^host__username")
    # this field is very useful for many to many field
    filter_horizontal = ("amenities", "facilities", "house_rules")
    
    def count_amenities(self, obj):
        #obj means current row
        return obj.amenities.count()
    
    def count_photos(self, obj):
        return obj.photos.count()
