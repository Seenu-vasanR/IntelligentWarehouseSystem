
from django import forms
from django.contrib import admin
from django.db import transaction
from django.db.models import F
from django.utils.html import format_html

from .models import Category, Product, Supplier, StockMovement


admin.site.register(Category)
admin.site.register(Supplier)


# STOCK STATUS FILTER
class StockStatusFilter(admin.SimpleListFilter):

    title = 'Stock Status'
    parameter_name = 'stock_status'

    def lookups(self, request, model_admin):
        return (
            ('in_stock', 'In Stock'),
            ('low_stock', 'Low Stock'),
            ('out_of_stock', 'Out of Stock'),
        )

    def queryset(self, request, queryset):

        if self.value() == 'in_stock':
            return queryset.filter(
                quantity__gt=F('minimum_stock')
            )

        if self.value() == 'low_stock':
            return queryset.filter(
                quantity__gt=0,
                quantity__lte=F('minimum_stock')
            )

        if self.value() == 'out_of_stock':
            return queryset.filter(quantity=0)

        return queryset


# PRODUCT ADMIN
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'product_name',
        'product_code',
        'category',
        'quantity',
        'minimum_stock',
        'colored_stock_status'
    )

    list_filter = ('category', StockStatusFilter)

    search_fields = ('product_name', 'product_code')

    @admin.display(description='Stock Status')
    def colored_stock_status(self, obj):

        status = obj.stock_status

        if status in ['Low Stock', 'Out of Stock']:
            return format_html(
                '<span style="color: red; font-weight: bold;">{}</span>',
                status
            )

        return format_html(
            '<span style="color: green; font-weight: bold;">{}</span>',
            status
        )


# STOCK MOVEMENT VALIDATION FORM
class StockMovementForm(forms.ModelForm):

    class Meta:
        model = StockMovement
        fields = '__all__'

    def clean(self):

        cleaned_data = super().clean()

        product = cleaned_data.get('product')
        movement_type = cleaned_data.get('movement_type')
        quantity = cleaned_data.get('quantity')

        if product and movement_type == 'OUT' and quantity:

            if quantity <= 0:
                self.add_error(
                    'quantity',
                    'Quantity must be greater than zero.'
                )

            elif product.quantity < quantity:
                raise forms.ValidationError(
                    'Insufficient stock available!'
                )

        return cleaned_data


# STOCK MOVEMENT ADMIN
@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):

    form = StockMovementForm

    list_display = (
        'product',
        'movement_type',
        'quantity',
        'movement_date'
    )

    search_fields = (
        'product__product_name',
        'product__product_code'
    )

    list_filter = (
        'movement_type',
        'movement_date'
    )

    date_hierarchy = 'movement_date'

    @transaction.atomic
    def save_model(self, request, obj, form, change):

        if not change:

            product = Product.objects.select_for_update().get(
                pk=obj.product_id
            )

            if obj.movement_type == 'IN':
                product.quantity += obj.quantity

            elif obj.movement_type == 'OUT':

                if product.quantity < obj.quantity:
                    raise forms.ValidationError(
                        'Insufficient stock available!'
                    )

                product.quantity -= obj.quantity

            product.save()

        super().save_model(request, obj, form, change)
