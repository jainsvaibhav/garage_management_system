
import datetime
from .utils import unique_slug_generator
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.core.validators import MaxValueValidator, MinValueValidator


def get_date_time():
    date = datetime.datetime.today()
    day = date.day
    months = {
        1: 'JAN', 2: 'FEB', 3: 'MAR', 4: 'APR', 5: 'MAY', 6: 'JUN',
        7: 'JUL', 8: 'AUG', 9: 'SEP', 10: 'OCT', 11: 'NOV', 12: 'DEC',
    }
    year = date.year
    year = str(year)
    year = year[-2:]
    bill_no = str(day)
    month = months[date.month]
    bill_no += month
    bill_no += year
    return bill_no


def generate_purchase_bill_no():
    bill_no = 'P'
    bill_no += get_date_time()
    # bill_no += 'PURC'
    obj = InvoicePurchase.objects.latest('date_time')
    print(obj)
    print(obj.date_time)
    print(datetime.datetime.today().day)
    print(obj.date_time.day)
    if obj.date_time.day == datetime.datetime.today().day:
    	print('in if ')
    	dt = obj.bill_no[-4:]
    	digit = int(dt)
    	digit += 1
    	digit = str(digit)
    	dg_len = len(digit)
    	zeros_len = 4 - dg_len
    	zeros = ''
    	for i in range(0, zeros_len):
    		zeros += '0'
    	bill_no += zeros
    	bill_no += digit
    else:
    	print('in else')
    	bill_no += '0001'
    return bill_no


def generate_sale_bill_no():
    bill_no = 'S'
    bill_no += get_date_time()
    # bill_no += 'SALE'
    obj = InvoiceSale.objects.latest('date_time')
    if obj.date_time.day == datetime.datetime.today().day:
    	dt = obj.bill_no[-4:]
    	digit = int(dt)
    	digit += 1
    	digit = str(digit)
    	dg_len = len(digit)
    	zeros_len = 4 - dg_len
    	zeros = ''
    	for i in range(0, zeros_len):
    		zeros += '0'
    	bill_no += zeros
    	bill_no += digit
    else:
    	bill_no += '0001'
    return bill_no


class VehicleDetails(models.Model):
	manufacturer = models.CharField(max_length=50)
	model_name = models.CharField('model', max_length=50)
	model_year = models.PositiveIntegerField()
	registration_no = models.CharField(max_length=15)
	chassis_no = models.CharField(max_length=15)
	slug = models.SlugField(null=True, blank=True)
	is_sold = models.BooleanField(default=False)
	color = models.CharField(max_length=10)
	

	def __str__(self):
		return self.model_name

	@property
	def title(self):
		return self.model_name

	def get_absolute_url(self):
		# return f"/vehicles/{self.slug}"
		return reverse('vehicles:detail', kwargs={'slug': self.slug})


class PartyDetails(models.Model):
	full_name = models.CharField(max_length=15)
	aadhar_no = models.CharField(max_length=12)
	phone_no = models.CharField(max_length=10)
	email = models.EmailField(
		max_length=140,
		default='NA',
		)
	address = models.CharField(
		max_length=200,
		default='NA',
		)
	is_buyer = models.BooleanField(default=False)
	is_seller = models.BooleanField(default=False)
	vehicle_detail = models.ForeignKey(VehicleDetails)
	slug = models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.full_name

	@property
	def title(self):
		return self.full_name


class InvoicePurchase(models.Model):
	bill_no = models.CharField(
		max_length=12,
		blank=True,
		default=generate_purchase_bill_no)
	party_purchased = models.ForeignKey(PartyDetails)
	amount_purchased = models.PositiveIntegerField()
	expense = models.PositiveIntegerField()
	valuation_amount = models.PositiveIntegerField()
	date_time = models.DateTimeField(default=datetime.datetime.today())

	def __str__(self):
		return self.bill_no + '-' + self.party_purchased.vehicle_detail.model_name



class InvoiceSale(models.Model):
	bill_no = models.CharField(
		max_length=12,
		blank=True,
		default=generate_sale_bill_no)
	purchase_bill_no = models.ForeignKey(InvoicePurchase)
	party_sold = models.ForeignKey(PartyDetails)
	amount_sold = models.PositiveIntegerField()
	date_time = models.DateTimeField()

	def __str__(self):
		return self.bill_no


class Accounting(models.Model):
	sale_bill_no = models.ForeignKey(InvoiceSale)
	gross_profit = models.PositiveIntegerField()


def vd_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)


pre_save.connect(vd_pre_save_receiver, sender=VehicleDetails)
pre_save.connect(vd_pre_save_receiver, sender=PartyDetails)
