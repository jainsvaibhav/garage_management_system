
# from .models import PartyDetails, InvoiceSale
import datetime


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


def generate_purchase_bill_no(instance, obj):
    bill_no = 'P'
    bill_no += get_date_time()
    # bill_no += 'PURC'
    # obj = InvoicePurchase.objects.latest('date_time')
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
    return bill_no


def generate_sale_bill_no(instance, obj):
    bill_no = 'S'
    bill_no += get_date_time()
    # bill_no += 'SALE'
    # obj = InvoiceSale.objects.latest('date_time')
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
    return bill_no
