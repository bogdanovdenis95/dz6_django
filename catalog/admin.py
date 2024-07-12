from django.contrib import admin
from .models import Category, Product, Version
from .admin_forms import AdminProductForm


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    form = AdminProductForm

    def category(self, obj):
        return obj.category.name

    category.short_description = 'Category'

admin.site.register(Version)
