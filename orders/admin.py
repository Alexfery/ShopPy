from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    raw_id_fields = ("product",)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email", "phone", "total_price", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("first_name", "last_name", "email", "phone", "address", "city", "county")
    inlines = [OrderItemInline]
