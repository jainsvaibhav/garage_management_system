from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import (
    UserLoginForm,
    UserRegisterForm,
    ChangeUserNameForm,
    ChangeEmailForm,
    ChangePasswordForm
)


# Create your views here.
def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        # print(request.user.is_authenticated())
        return redirect('/vehicles/')
    return render(request, 'accounts/login_form.html', {'form': form})


def register_view(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
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


@login_required(login_url='/accounts/login/')
def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')


@login_required(login_url='/accounts/login/')
def change_fullname_view(request):
    form = ChangeUserNameForm(request.POST or None)
    if form.is_valid():
        user = User.objects.get(id=request.user.id)
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return redirect('/profiles/')
    return render(request, 'accounts/change_name_form.html', {'form': form})


@login_required(login_url='/accounts/login/')
def change_email_view(request):
    form = ChangeEmailForm(request.POST or None)
    if form.is_valid():
        user = User.objects.get(id=request.user.id)
        new_email = form.cleaned_data.get('new_email')
        user.email = new_email
        user.save()
        return redirect('/profiles/')
    return render(request, 'accounts/change_email_form.html', {'form': form})


@login_required(login_url='/accounts/login/')
def change_password_view(request):
    form = ChangePasswordForm(request.POST or None, user=request.user)
    if form.is_valid():
        user = User.objects.get(id=request.user.id)
        new_password = form.cleaned_data.get('new_password')
        user.set_password(new_password)
        user.save()
        return redirect('/profiles/')
    return render(request, 'accounts/change_password_form.html', {'form': form})
