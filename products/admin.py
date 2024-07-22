from django.contrib import admin
from .models import Category, Product
from import_export.admin import ImportExportModelAdmin


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('category_name', 'slug', 'description', 'created_at')
    list_display_links = ('category_name', 'slug', 'description', 'created_at')
    search_fields = ('category_name', 'slug')
    ordering = ('created_at',)
    prepopulated_fields = {'slug': ('category_name',)}


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('name', 'category', 'slug', 'price', 'description', 'value', 'count', 'rating', 'Featured_products', 'created_at')
    list_display_links = ('name', 'category', 'slug', 'price', 'description', 'count', 'rating', 'Featured_products', 'created_at')
    search_fields = ('name', 'description', 'slug', 'category')
    ordering = ('created_at',)
    prepopulated_fields = {'slug': ('name',)}
