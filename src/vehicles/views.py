
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template.loader import get_template

from django.views import View
from django.views.generic import CreateView, DetailView, ListView, TemplateView 
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import InvoicePurchaseCreateForm, PartyDetailsCreateForm, VehicleDetailsCreateForm
from .models import InvoicePurchase, InvoiceSale, PartyDetails, VehicleDetails
from .utils import render_to_pdf 



@login_required(login_url='/accounts/login/')
def invoice_purchase_createview(request):
	form = InvoicePurchaseCreateForm(None or request.POST)
	errors = None
	if form.is_valid():
		# obj = InvoicePurchaseCreateForm
		form.date_time = datetime.datetime.today()
		form.save()
		return HttpResponseRedirect('/vehicles/')
	if form.errors:
		errors = form.errors
	
	template_name = 'vehicles/invoice_purchase_create_form.html'
	context = {
				'form': form,
				'errors': errors,
	}
	return render(request, template_name, context)


# class AddVehicleCreateView(LoginRequiredMixin, CreateView):
#     form_class = VehicleDetailsCreateForm
#     login_url = '/accounts/login/'
#     template_name = 'add_vehicle_create_form.html'
#     success_url = reverse_lazy('vehicles:add-party')

#     def form_valid(self, form):
#         instance = form.save(commit=False)
#         # instance.owner = self.request.user
#         return super(VehicleDetailsCreateForm, self).form_valid(form)

#     def get_context_data(self, *args, **kwargs):
#         context = super(VehicleDetailsCreateForm, self).get_context_data(*args, **kwargs)
#         context['title'] = 'Add Vehicle'
#         return context

@login_required(login_url='/accounts/login/')
def add_vehicle_createview(request):
	form = VehicleDetailsCreateForm(None or request.POST)
	errors = None
	if form.is_valid():
		# obj = InvoicePurchaseCreateForm
		print(form)
		form.save()
		return HttpResponseRedirect('/vehicles/add-party/')
	if form.errors:
		errors = form.errors
	
	template_name = 'vehicles/add_vehicle_create_form.html'
	context = {
				'form': form,
				'errors': errors,
	}
	return render(request, template_name, context)


@login_required(login_url='/accounts/login/')
def add_party_seller_createview(request):
	form = PartyDetailsCreateForm(None or request.POST, initial={'is_seller': True})
	errors = None
	if form.is_valid():
		print(form.cleaned_data)
		print(form.is_bound)
		form.cleaned_data['is_seller'] = True
		# obj = InvoicePurchaseCreateForm
		# form.is_seller = True
		print(form.cleaned_data['is_seller'])
		print(form.cleaned_data)
		form.save()
		return HttpResponseRedirect('/vehicles/invoice-purchase/')
	if form.errors:
		errors = form.errors
	
	template_name = 'vehicles/add_seller_create_form.html'
	context = {
				'form': form,
				'errors': errors,
	}
	return render(request, template_name, context)

# Create your views here.
@login_required(login_url='/accounts/login/')
def vehicles_purchased_listview(request):
	# print('hello_sold')
	template_name = 'vehicles/vehicles_list_purchased.html'
	queryset = VehicleDetails.objects.filter(is_sold=False)
	context = {
		"vehicles_list": queryset
	}
	return render(request, template_name, context)


@login_required(login_url='/accounts/login/')
def vehicles_sold_listview(request):
	print('hello')
	template_name = 'vehicles/vehicles_list_sold.html'
	queryset = VehicleDetails.objects.filter(is_sold=True)
	context = {
		"vehicles_list": queryset
	}
	return render(request, template_name, context)


@login_required(login_url='/accounts/login/')
def parties_listview(request):
	template_name = 'parties/parties_list.html'
	queryset = PartyDetails.objects.all()
	context = {
		"parties_list": queryset
	}
	return render(request, template_name, context)


@login_required(login_url='/accounts/login/')
def add_vehilceform_view(request):
    form = (request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        # this is required step before login
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/vehicles/')
    return render(request, 'accounts/register_form.html', {'form': form})


def vehicle_addview(request):
	return HttpResponse('add vehicles')


def bills_view(request):
	return HttpResponse('bills listed here')


@login_required(login_url='/accounts/login/')
def vehicle_purchased_detailsview(request, **kwargs):
	slug = kwargs.get('slug')
	template_name = 'vehicles/vehicle_details.html'
	# slug = get_object_or_404(VehicleDetails, slug)
	queryset = VehicleDetails.objects.get(slug=slug)
	party_details = PartyDetails.objects.get(vehicle_detail_id=queryset.id)
	bill_p = InvoicePurchase.objects.get(party_purchased_id=party_details.id)
	context = {
		"vehicle": queryset,
		"bill_p": bill_p,
	}
	return render(request, template_name, context)


def vehicle_sold_detailsview(request, **kwargs):
	slug = kwargs.get('slug')
	template_name = 'vehicles/vehicle_details.html'
	# slug = get_object_or_404(VehicleDetails, slug)
	queryset = VehicleDetails.objects.get(slug=slug)
	party_details = PartyDetails.objects.filter(is_seller=True).get(vehicle_detail_id=queryset.id)
	bill_p = InvoicePurchase.objects.get(party_purchased_id=party_details.id)
	bill_s = InvoiceSale.objects.get(purchase_bill_no_id=bill_p.id)
	context = {
		"vehicle": queryset,
		"bill_p": bill_p,
		"bill_s": bill_s,
	}
	return render(request, template_name, context)


@login_required(login_url='/accounts/login/')
def party_seller_detailsview(request, **kwargs):
	slug = kwargs.get('slug')
	template_name = 'parties/party_details.html'
	# slug = get_object_or_404(VehicleDetails, slug)
	queryset = PartyDetails.objects.get(slug=slug)
	bill = InvoicePurchase.objects.get(party_purchased_id=queryset.id)
	context = {
		"party": queryset,
		"bill": bill,
	}
	return render(request, template_name, context)


@login_required(login_url='/accounts/login/')
def party_buyer_detailsview(request, **kwargs):
	slug = kwargs.get('slug')
	template_name = 'parties/party_details.html'
	# slug = get_object_or_404(VehicleDetails, slug)
	queryset = PartyDetails.objects.get(slug=slug)
	bill = InvoiceSale.objects.get(party_sold_id=queryset.id)
	context = {
		"party": queryset,
		"bill": bill,
	}
	return render(request, template_name, context)


class VehicleDetailsUpdate(UpdateView):
    model = VehicleDetails
    template_name = 'vehicles/update_vehicle_form.html'
    fields = ['manufacturer',
    		  'model_name',
    		  'model_year',
    		  'color',
    		  'registration_no',
    		  'chassis_no',
    		]
    success_url = reverse_lazy('vehicles:purchased-list')


class VehicleDelete(DeleteView):
    model = VehicleDetails
    success_url = reverse_lazy('vehicles:purchased-list')


class SellerDetailsUpdate(UpdateView):
	model = PartyDetails
	template_name = 'vehicles/update_seller_form.html'
	fields = [
				'full_name',
				'aadhar_no',
				'phone_no',
				'email',
				'address',
				'vehicle_detail',
				'is_seller',
				]
	success_url = reverse_lazy('parties:list')


# class PurchaseInvoiceDetailsUpdate(UpdateView):
# 	model = InvoicePurchase
# 	success_url = reverse_lazy('vehicles:purchased-list')
# 	fields = [
# 				'amount_purchased',
# 				'expense',
# 				'valuation_amount',
# 				'party_purchased',
# 				# 'vehicle_detail',
				
# 			]
#     # success_url = reverse_lazy('')  
# 	def get_queryset(self):
		# slug = self.kwargs.get("slug")
# 		queryset = VehicleDetails.objects.get(slug=slug)
# 		party_details = PartyDetails.objects.get(vehicle_detail_id=queryset.id)
# 		# bill_p = InvoicePurchase.objects.get(party_purchased_id=party_details.id)
# 		return InvoicePurchase.objects.get(party_purchased_id=party_details.id)

# def update_vehicle_purchased_detailsview(request, **kwargs):
# 	slug = kwargs.get('slug')
# 	template_name = 'vehicles/vehicle_details.html'
# 	# slug = get_object_or_404(VehicleDetails, slug)
# 	queryset = VehicleDetails.objects.get(slug=slug)
# 	party_details = PartyDetails.objects.get(vehicle_detail_id=queryset.id)
# 	bill_p = InvoicePurchase.objects.get(party_purchased_id=party_details.id)
# 	context = {
# 		"vehicle": queryset,
# 		"bill_p": bill_p,
# 	}
# 	return render(request, template_name, context)



class GeneratePdfPurchaseInvoice(View):
	def get(self, request, *args, **kwargs):
		slug = kwargs.get('slug')
		template = get_template('pdf/purchase_invoice.html')
		queryset = VehicleDetails.objects.get(slug=slug)
		party_details = PartyDetails.objects.get(vehicle_detail_id=queryset.id)
		bill_p = InvoicePurchase.objects.get(party_purchased_id=party_details.id)
		context = {
				'seller_full_name': bill_p.party_purchased.full_name,
				'seller_phone_no': bill_p.party_purchased.phone_no,
				'seller_email': bill_p.party_purchased.email,
				'seller_address': bill_p.party_purchased.address,
				'seller_aadhar_no': bill_p.party_purchased.aadhar_no,
				'vehicle_manufacturer': bill_p.party_purchased.vehicle_detail.manufacturer,
				'vehicle_model_name': bill_p.party_purchased.vehicle_detail.model_name,
				'vehicle_model_year': bill_p.party_purchased.vehicle_detail.model_year,
				'vehicle_color': bill_p.party_purchased.vehicle_detail.color,
				'vehicle_registration_no': bill_p.party_purchased.vehicle_detail.registration_no,
				'vehicle_chassis_no': bill_p.party_purchased.vehicle_detail.chassis_no,
				'invoice_no': bill_p.bill_no,
				'amount_purchased': bill_p.amount_purchased,
				'date_time': bill_p.date_time,
		}
		html = template.render(context)
		pdf = render_to_pdf('pdf/purchase_invoice.html', context)
		if pdf:
			response = HttpResponse(pdf, content_type='application/pdf')
			filename = "Invoice_%s.pdf" %(bill_p.bill_no)
			content = "inline; filename='%s'" %(filename)
			download = request.GET.get("download")
			if download:
				content = "attachment; filename='%s'" %(filename)
			response['Content-Disposition'] = content
			return response
		return HttpResponse("Not found")


class GeneratePdfSalesInvoice(View):
	def get(self, request, *args, **kwargs):
		slug = kwargs.get('slug')
		template = get_template('pdf/sales_invoice.html')
		queryset = VehicleDetails.objects.get(slug=slug)
		party_details = PartyDetails.objects.filter(is_buyer=True).get(vehicle_detail_id=queryset.id)
		# bill_p = InvoicePurchase.objects.get(party_purchased_id=party_details.id)
		bill_s = InvoiceSale.objects.get(party_sold_id=party_details.id)
		context = {
				'buyer_full_name': bill_s.party_sold.full_name,
				'buyer_phone_no': bill_s.party_sold.phone_no,
				'buyer_email': bill_s.party_sold.email,
				'buyer_address': bill_s.party_sold.address,
				'buyer_aadhar_no': bill_s.party_sold.aadhar_no,
				'vehicle_manufacturer': bill_s.party_sold.vehicle_detail.manufacturer,
				'vehicle_model_name': bill_s.party_sold.vehicle_detail.model_name,
				'vehicle_model_year': bill_s.party_sold.vehicle_detail.model_year,
				'vehicle_color': bill_s.party_sold.vehicle_detail.color,
				'vehicle_registration_no': bill_s.party_sold.vehicle_detail.registration_no,
				'vehicle_chassis_no': bill_s.party_sold.vehicle_detail.chassis_no,
				'invoice_no': bill_s.bill_no,
				'amount_sold': bill_s.amount_sold,
				'date_time': bill_s.date_time,
		}
		html = template.render(context)
		pdf = render_to_pdf('pdf/sales_invoice.html', context)
		if pdf:
			response = HttpResponse(pdf, content_type='application/pdf')
			filename = "Invoice_%s.pdf" %(bill_s.bill_no)
			content = "inline; filename='%s'" %(filename)
			download = request.GET.get("download")
			if download:
				content = "attachment; filename='%s'" %(filename)
			response['Content-Disposition'] = content
			return response
		return HttpResponse("Not found")
