from django.contrib import admin
from . models import Category, Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'image']
    prepopulated_fields = {'slug': ['name']}
admin.site.register(Category,CategoryAdmin)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'description', 'price', 'category', 'image', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ['name']}
    list_per_page = 20
admin.site.register(Product,ProductAdmin)
