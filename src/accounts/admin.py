from django.contrib import admin

from .models import Customer, Venue

# Register your models here.

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ['id', 'organization_name', 'email', 'username', 'phone_num', 'terms_condition']

    def email(self, obj):
        return obj.user.email

    def username(self, obj):
        return obj.user.username

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'username', 'phone_num', 'terms_condition']

    def email(self, obj):
        return obj.user.email

    def username(self, obj):
        return obj.user.username