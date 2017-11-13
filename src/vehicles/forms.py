from django.forms import ModelForm
from django import forms
from .models import InvoicePurchase, InvoiceSale, PartyDetails, VehicleDetails


class InvoicePurchaseCreateForm(forms.ModelForm):
    class Meta:
        model = InvoicePurchase
        fields = [
                    'amount_purchased',
                    'expense',
                    'valuation_amount',
                    'party_purchased',
                    # 'vehicle_detail',
        ]

class PartyDetailsCreateForm(forms.ModelForm):
    class Meta:
        model = PartyDetails
        fields = [
                    'full_name',
                    'aadhar_no',
                    'phone_no',
                    'email',
                    'address',
                    'vehicle_detail',
                    'is_seller',
        ]


class VehicleDetailsCreateForm(forms.ModelForm):
    class Meta:
        model = VehicleDetails
        fields = [
                    'manufacturer',
                    'model_name',
                    'model_year',
                    'color',
                    'registration_no',
                    'chassis_no',
        ]
# class PartyDetailsForm(forms.ModelForm):
#     email = forms.EmailField(label='Email Address')
#     first_name = forms.CharField(label='First Name')
#     last_name = forms.CharField(label='Last Name')
#     confirm_password = forms.CharField(
#         widget=forms.PasswordInput,
#         label='Confirm Password'
#     )
#     aadhar_no = forms. 
# 	class Meta:
# 		model = PartyDetails
# 		fields = [
# 			'first_name',
# 			'last_name',
# 			'aadhar_no',
# 			'address',
# 			'phone_no',
# 			'email'
# 		]

# 	# def clean_confirm_password(self):
# 	# 	email = self.cleaned_data.get('email')
# 	# 	password = self.cleaned_data.get('password')
# 	# 	confirm_password = self.cleaned_data.get('confirm_password')
# 	# 	if password != confirm_password:
# 	# 		raise forms.ValidationError('Passwords do not match')
# 	# 	check_email = UserDetails.objects.filter(email=email)
# 	# 	if check_email.exists():
# 	# 		raise forms.ValidationError('This email has already been taken')
# 	# 	return email

# class UserRegisterForm(forms.ModelForm):
#     email = forms.EmailField(label='Email Address')
#     first_name = forms.CharField(label='First Name')
#     last_name = forms.CharField(label='Last Name')
#     confirm_password = forms.CharField(
#         widget=forms.PasswordInput,
#         label='Confirm Password'
#     )
#     class Meta:
#         model = User
#         fields = [
#             'first_name',
#             'last_name',
#             'email',
#         ]

#     def clean_confirm_password(self):
#         email = self.cleaned_data.get('email')
#         password = self.cleaned_data.get('password')
#         confirm_password = self.cleaned_data.get('confirm_password')
#         if password != confirm_password:
#             raise forms.ValidationError('Passwords do not match')
#         check_email = User.objects.filter(email=email)
#         if check_email.exists():
#             raise forms.ValidationError('This email has already been taken')
#         return email