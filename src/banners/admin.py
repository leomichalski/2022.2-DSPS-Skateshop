from django.contrib import admin
from .models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):

    def admin_banner(self):
        if self.title:
            return self.title
        elif not self.title and self.description:
            if len(self.description) > 50:
                return self.description[:50] + '...'
            return self.description
        return self.photo

    def admin_is_in_homepage(self):
        if self.is_in_homepage:
            return 'Sim'
        return 'Não'

    def admin_homepage_priority(self):
        return self.homepage_priority

    admin_banner.short_description = 'Banner'
    admin_is_in_homepage.short_description = 'Está na home?'
    admin_homepage_priority.short_description = 'Prioridade na home (maior = primeiro)'

    admin_banner.admin_order_field = '-photo'
    admin_is_in_homepage.admin_order_field = '-is_in_homepage'
    admin_homepage_priority.admin_order_field = '-homepage_priority'

    list_display = (
        admin_banner,
        admin_is_in_homepage,
        admin_homepage_priority,
    )
