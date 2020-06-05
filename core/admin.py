from django.contrib import admin
from .models import Item, Order, OrderItem


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price', 'category']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Order)
admin.site.register(OrderItem)
