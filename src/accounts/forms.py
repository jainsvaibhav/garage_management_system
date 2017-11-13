from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exists')

            if not user.check_password(password):
                raise forms.ValidationError('Password incorrect')

        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email Address')
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label='Confirm Password'
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'confirm_password'
        ]

    def clean_confirm_password(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match')
        check_email = User.objects.filter(email=email)
        if check_email.exists():
            raise forms.ValidationError('This email has already been taken')
        return email


class ChangeUserNameForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
        ]

    def clean(self, *args, **kwargs):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        if not first_name:
            raise forms.ValidationError('Enter first name')
        if not last_name:
            raise forms.ValidationError('Enter last name')
        return super(ChangeUserNameForm, self).clean(*args, **kwargs)


class ChangeEmailForm(forms.ModelForm):
    new_email = forms.EmailField(label='New Email Address')
    confirm_email = forms.EmailField(label='Confirm Address')

    class Meta:
        model = User
        fields = [
            'new_email',
            'confirm_email',
        ]

    def clean(self, *args, **kwargs):
        new_email = self.cleaned_data.get('new_email')
        confirm_email = self.cleaned_data.get('confirm_email')
        if new_email != confirm_email:
            raise forms.ValidationError('Emails do not match!')
        return super(ChangeEmailForm, self).clean(*args, **kwargs)


class ChangePasswordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    current_password = forms.CharField(
        widget=forms.PasswordInput,
        label='Current Password'
    )

    new_password = forms.CharField(
        widget=forms.PasswordInput,
        label='New Password'
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label='Confirm Password'
    )

    class Meta:
        model = User
        fields = [
            'current_password',
            'new_password',
            'confirm_password',
        ]

    def clean(self, *args, **kwargs):
        user = User.objects.get(id=self.user.id)
        # user_password = self.user.check_password(user.password)
        # print(user_password)
        current_password = self.cleaned_data.get('current_password')
        user_password = self.user.check_password(current_password)
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if not user_password:
            raise forms.ValidationError('Password incorrect!')
        if new_password != confirm_password:
            raise forms.ValidationError('Passwords do not match!')
        return super(ChangePasswordForm, self).clean(*args, **kwargs)
