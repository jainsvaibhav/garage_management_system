from django.conf.urls import url
from django.views.generic import TemplateView

from .views import (
	vehicles_purchased_listview,
	vehicle_purchased_detailsview,
	vehicle_sold_detailsview,
	vehicle_addview,
	bills_view,
	add_vehilceform_view,
	vehicles_sold_listview,
	invoice_purchase_createview,
	add_vehicle_createview,
	add_party_seller_createview,
	VehicleDetailsUpdate,
	VehicleDelete,
	# PurchaseInvoiceDetailsUpdate,
	GeneratePdfPurchaseInvoice,
	GeneratePdfSalesInvoice,
)

urlpatterns = [
	url(r'^purchased/(?P<slug>[\w-]+)/details/$', vehicle_purchased_detailsview, name='purchased-details'),
	url(r'^sold/(?P<slug>[\w-]+)/print/$', GeneratePdfSalesInvoice.as_view(), name='invoice-sales-print'),
	url(r'^purchased/(?P<slug>[\w-]+)/print/$', GeneratePdfPurchaseInvoice.as_view(), name='invoice-purchase-print'),
	url(r'^purchased/(?P<slug>[\w-]+)/delete/$', VehicleDelete.as_view(), name='vehicle-delete'),
	url(r'^purchased/(?P<slug>[\w-]+)/update/$', VehicleDetailsUpdate.as_view(), name='vehicle-update'),
	url(r'add-vehicle/$', add_vehicle_createview, name='add-vehicle'),
	url(r'purchase-vehicle/$', TemplateView.as_view(template_name='vehicles/purchase_vehicle.html'), name='purchase-vehicle'),
	url(r'add-party/$', add_party_seller_createview, name='add-party'),
	url(r'invoice-purchase/$', invoice_purchase_createview, name='invoice-purchase'),
	url(r'bills/$', bills_view, name='bills'),
	url(r'sold/$', vehicles_sold_listview, name='sold-list'),
	url(r'^sold/(?P<slug>[\w-]+)/details/$', vehicle_sold_detailsview, name='sold-details'),
	url(r'$', vehicles_purchased_listview, name='purchased-list'),

]
