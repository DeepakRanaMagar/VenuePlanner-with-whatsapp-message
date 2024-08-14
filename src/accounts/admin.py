from django.contrib import admin

from .models import Customer, Media, Venue

# Register your models here.

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    # list_display = ['auth_id','id', 'organization_name', 'email', 'username','logo'
    #                 ,'property_type', 'phone_num', 'pan_no', 'full_address' 
    #                 , 'rating', 'price','seat_capacity','photo1', 'video1',
    #                 'terms_condition', 'isSubscribed'
    #                 , 'social1', 'social2', 'social3']

    list_display = ['id', 'organization_name', 'email', 'username','address','logo'
                    ,'property_type', 'phone_num', 'pan_no', 'rating', 'price','seat_capacity','photo1', 'video1',
                    'terms_condition', 'isSubscribed'
                    , 'social1', 'social2', 'social3']
    def email(self, obj):
        return obj.user.email

    def username(self, obj):
        return obj.user.username
    
    def auth_id(self, obj):
        return obj.user.id
    auth_id.short_description = 'Auth'

    # def is_Subscribed(self, obj):
    #     return Venue.isSubscribed
    # is_Subscribed.short_description = 'Subscribed'
    # # is_Subscribed.boolean = True
    
    # def full_address(self, obj):
    #     return f"{obj.province}, {obj.district}, {obj.municipality}, {obj.ward}"
    # full_address.short_description = 'Address'

    fieldsets = (
        (None, {
            'fields': ('organization_name','phone_num', 'pan_no', 'photo1', 'video1', 'property_type', 'isSubscribed', 'photo2', 'video2', 'rating', 'price'
                    ,'seat_capacity', 'social1', 'social2', 'social3')
        }),
        ('Address', {
            'fields': ('province', 'district', 'municipality', 'ward'),
            'classes': ('collapse',),
        }),
    )

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    # list_display = ['auth_id','id', 'full_name', 'email', 'username', 'phone_num', 'terms_condition']
    list_display = ['id', 'full_name', 'email', 'username', 'phone_num', 'terms_condition']

    def email(self, obj):
        return obj.user.email

    def username(self, obj):
        return obj.user.username

    def auth_id(self, obj):
        return obj.user.id
    auth_id.short_description = 'Auth'

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['venue','photo', 'video']