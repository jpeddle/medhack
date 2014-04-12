from django.contrib import admin
from src.apps.admin.models import BillingAddress, Insurance

class BillingAddressAdmin(admin.ModelAdmin):
    pass

class InsuranceAdmin(admin.ModelAdmin):
    pass

admin.site.register(BillingAddress, BillingAddressAdmin)
admin.site.register(Insurance, InsuranceAdmin)
