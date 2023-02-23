from django.contrib import admin
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    def admin_name(self):
        return self.name

    def admin_insta(self):
        if len(self.insta) > 10:
            return self.insta[:10] + '...'
        return self.insta

    def admin_youtube(self):
        if len(self.youtube) > 10:
            return self.youtube[:10] + '...'
        return self.youtube

    def admin_email(self):
        if len(self.email) > 10:
            return self.email[:10] + '...'
        return self.email

    def admin_phone(self):
        if len(self.phone) > 10:
            return self.phone[:10] + '...'
        return self.phone

    def admin_business_hours(self):
        if len(self.business_hours) > 10:
            return self.business_hours[:10] + '...'
        return self.business_hours

    def admin_address(self):
        if len(self.address) > 10:
            return self.address[:10] + '...'
        return self.address

    admin_name.short_description = 'Nome'
    admin_insta.short_description = 'Instagram'
    admin_youtube.short_description = 'YouTube'
    admin_email.short_description = 'Email'
    admin_phone.short_description = 'Celular'
    admin_business_hours.short_description = 'Horário de funcionamento'
    admin_address.short_description = 'Endereço'

    admin_name.admin_order_field = '-name'
    admin_insta.admin_order_field = '-insta'
    admin_youtube.admin_order_field = '-youtube'
    admin_email.admin_order_field = '-email'
    admin_phone.admin_order_field = '-phone'
    admin_business_hours.admin_order_field = '-business_hours'
    admin_address.admin_order_field = '-address'

    list_display = (
        admin_name,
        admin_insta,
        admin_youtube,
        admin_email,
        admin_phone,
        admin_business_hours,
        admin_address,
    )
