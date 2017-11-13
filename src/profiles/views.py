from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    context = {}
    if request.user.is_authenticated():
        context['username'] = request.user.username
        context['first_name'] = request.user.first_name
        context['last_name'] = request.user.last_name
        context['email'] = request.user.email
    return render(request, 'profiles/index.html', context)
