from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Card


@login_required
def index(request):
    # request.user.is_authenticated
    # card = Card(child_name='Артём', creator_id=request.user, date=timezone.now())
    # card.save()
    cards_data = Card.objects.all()
    indexs = range(len(cards_data))
    return render(request, 'main/index.html', {'cards_data' : cards_data, 'indexs': indexs})


@login_required
def info(request):
    return render(request, 'main/info.html')


@login_required
def contact(request):
    return render(request, 'main/contact.html')


