from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home_view(request):
     return render(request, 'home.html')

from django.contrib.auth.decorators import permission_required

@permission_required('myapp.view_special_page')
def special_page_view(request):
    return render(request, 'special_page.html')