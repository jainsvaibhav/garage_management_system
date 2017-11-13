from django.contrib import admin
# Register your models here.
from vehicles.models import VehicleDetails, PartyDetails, InvoicePurchase, InvoiceSale, Accounting

admin.site.register(VehicleDetails)
admin.site.register(PartyDetails)
admin.site.register(InvoicePurchase)
admin.site.register(InvoiceSale)
admin.site.register(Accounting)

