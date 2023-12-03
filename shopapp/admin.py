from django.contrib import admin
from .models import Product, Client, Order


@admin.action(description="сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


@admin.action(description="товар оплачен")
def is_paid(modeladmin, request, queryset):
    queryset.update(is_paid=True)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_product', 'quantity', 'cost']
    ordering = ['name_product', '-quantity']
    list_filter = ['date_add_product', 'cost']
    search_fields = ['name_product', 'description_product']
    search_help_text = 'поиск продукции по наименованию'
    actions = [reset_quantity]
    readonly_fields = ['date_add_product']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name_product'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'описание товара',
                'fields': ['description_product'],
            },
        ),
        (
            'бухгалтерия',
            {
                'fields': ['cost', 'quantity'],
            },
        ),

    ]


class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_client', 'phone_number']
    ordering = ['id']
    search_fields = ['name_client', 'phone_number']
    search_help_text = 'поиск клиента по имени или телефону'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'buyer', 'total_cost', 'is_paid']
    ordering = ['-id']
    list_filter = ['date_create_order', 'total_cost', 'is_paid']
    search_fields = ['date_create_order']
    search_help_text = 'поиск заказа дате'
    actions = [is_paid]
    readonly_fields = ['date_create_order']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['buyer'],
            },
        ),
        (
            'Продукция',
            {
                'classes': ['collapse'],
                'description': 'продукция',
                'fields': ['products'],
            },
        ),
        (
            'бухгалтерия',
            {
                'fields': ['total_cost', 'is_paid', ],
            },
        ),

    ]


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
