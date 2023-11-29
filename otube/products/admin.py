from django.contrib import admin
from .models import Product, ProductCategory, Library


admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'description')
    fields = ('title', 'description', 'image', 'video_url', 'category')


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    pass
