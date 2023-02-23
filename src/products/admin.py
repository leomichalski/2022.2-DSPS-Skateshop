from django.contrib import admin
from .models import Product, Category, LimitedTimeOffer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    def admin_name(self):
        return self.name

    def admin_is_in_homepage(self):
        if self.is_in_homepage:
            return 'Sim'
        return 'Não'

    def admin_homepage_priority(self):
        return self.homepage_priority

    admin_name.short_description = 'Nome'
    admin_is_in_homepage.short_description = 'Está na home?'
    admin_homepage_priority.short_description = 'Prioridade na home (quanto maior, mais em cima)'

    admin_name.admin_order_field = '-name'
    admin_is_in_homepage.admin_order_field = '-is_in_homepage'
    admin_homepage_priority.admin_order_field = '-homepage_priority'

    list_display = (
        admin_name,
        admin_is_in_homepage,
        admin_homepage_priority,
    )


@admin.register(LimitedTimeOffer)
class LimitedTimeOfferAdmin(admin.ModelAdmin):

    def admin_start_datetime(self):
        return self.start_datetime

    def admin_end_datetime(self):
        return self.end_datetime

    def admin_relative_discount(self):
        if self.relative_discount is None:
            return 'N/A'
        return str(self.relative_discount) + '%'

    def admin_absolute_discount(self):
        if self.absolute_discount is None:
            return 'N/A'
        return 'R$' + str(self.absolute_discount)

    admin_start_datetime.short_description = 'Início'
    admin_end_datetime.short_description = 'Término'
    admin_relative_discount.short_description = 'Desconto relativo'
    admin_absolute_discount.short_description = 'Desconto absoluto'

    admin_start_datetime.admin_order_field = '-start_datetime'
    admin_end_datetime.admin_order_field = '-end_datetime'
    admin_relative_discount.admin_order_field = '-relative_discount'
    admin_absolute_discount.admin_order_field = '-absolute_discount'

    list_display = (
        admin_start_datetime,
        admin_end_datetime,
        admin_relative_discount,
        admin_absolute_discount,
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def admin_category(self):
        return self.category

    def admin_name(self):
        return self.name

    def admin_base_price(self):
        return self.base_price

    def admin_price(self):
        return self.price

    def admin_is_available(self):
        if self.is_available:
            return 'Sim'
        return 'Não'

    def admin_is_in_homepage(self):
        if self.is_in_homepage:
            return 'Sim'
        return 'Não'

    def admin_has_discount(self):
        if self.has_discount:
            return 'Sim'
        return 'Não'

    admin_category.short_description = 'Categoria'
    admin_name.short_description = 'Nome'
    admin_base_price.short_description = 'Preço Base'
    admin_price.short_description = 'Preço Atual'
    admin_is_available.short_description = 'Está disponível?'
    admin_is_in_homepage.short_description = 'Aparece na home?'
    admin_has_discount.short_description = 'Está em promoção?'

    admin_category.admin_order_field = '-category'
    admin_name.admin_order_field = '-name'
    admin_base_price.admin_order_field = '-base_price'
    admin_is_available.admin_order_field = '-is_available'
    admin_is_in_homepage.admin_order_field = '-is_in_homepage'

    list_display = (
        admin_name,
        admin_category,
        admin_base_price,
        admin_price,
        admin_has_discount,
        admin_is_available,
        admin_is_in_homepage,
    )

    search_fields = [
        'name',
        'description',
        'base_price',
    ]
