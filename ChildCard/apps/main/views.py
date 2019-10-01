from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    # request.user.is_authenticated
    return render(request, 'main/index.html')


@login_required
def info(request):
    return render(request, 'main/info.html')


@login_required
def contact(request):
    return render(request, 'main/contact.html')


