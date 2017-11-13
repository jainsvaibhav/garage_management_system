from django.conf.urls import url
from .views import (
	parties_listview,
	party_seller_detailsview,
	party_buyer_detailsview,
	SellerDetailsUpdate,
)

urlpatterns = [
	url(r'^seller/(?P<slug>[\w-]+)/update/$', SellerDetailsUpdate.as_view(), name='seller-update'),
	url(r'^seller/(?P<slug>[\w-]+)/$', party_seller_detailsview, name='seller-details'),
	url(r'^buyer/(?P<slug>[\w-]+)/$', party_buyer_detailsview, name='buyer-details'),
	url(r'$', parties_listview, name='list'),

]
