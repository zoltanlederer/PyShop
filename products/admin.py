from django.contrib import admin
from .models import Product, Offer


# Customizing the admin
class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


# Customizing the admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


# Register your models here.
admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)


