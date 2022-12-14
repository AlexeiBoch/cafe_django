from django.contrib import admin
from shop.models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'created', 'updated']
    list_filter = ['created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)