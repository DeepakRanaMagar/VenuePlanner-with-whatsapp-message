from django.contrib import admin

from .models import Customer, Venue

# Register your models here.

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ['auth_id', 'organization_name', 'email', 'username','property_type', 'phone_num', 'pan_no', 'full_address' ,'photo1', 'video1','terms_condition']

    def email(self, obj):
        return obj.user.email

    def username(self, obj):
        return obj.user.username
    
    def auth_id(self, obj):
        return obj.user.id
    auth_id.short_description = 'Auth'

    def full_address(self, obj):
        return f"{obj.province}, {obj.district}, {obj.municipality}, {obj.ward}"
    full_address.short_description = 'Address'

    fieldsets = (
        (None, {
            'fields': ('organization_name', 'pan_no', 'photo1', 'video1', 'property_type')
        }),
        ('Address', {
            'fields': ('province', 'district', 'municipality', 'ward'),
            'classes': ('collapse',),
        }),
    )

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['auth_id', 'full_name', 'email', 'username', 'phone_num', 'terms_condition']

    def email(self, obj):
        return obj.user.email

    def username(self, obj):
        return obj.user.username

    def auth_id(self, obj):
        return obj.user.id
    auth_id.short_description = 'Auth'