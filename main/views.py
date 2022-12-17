from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def dashboard_view(request):
    """ Dashboard page """
    return render(request, 'main/base.html', {})