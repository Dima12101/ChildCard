import os
import io
import ftplib
import json
import requests

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required

from django.utils import timezone

from .models import Card

from PIL import Image

ROOT_STATIC_APP = f'{settings.PROJECT_ROOT}/static'


@login_required
def index(request):
    cards_data = Card.objects.filter(creator_id=request.user)
    indexes = range(len(cards_data))
    return render(request, 'main/index.html', {'cards_data': cards_data,
                                               'indexes': indexes})


@login_required
def create_card_form(request):
    return render(request, 'main/create_card.html')


@login_required
def create_card_complete(request):
    photo_label, photo_format = request.FILES['photo'].name.rsplit('.', 1)
    if photo_format not in ['jpg', 'png']:
        return render(request, 'main/create_card.html')

    child_card = Card(
        child_name=request.POST['childname'],
        gender=int(request.POST['gender']),
        creator_id=request.user
    )
    child_card.save()

    photo_label = f"{photo_label}_{child_card.global_id}"
    photo_name = f"{photo_label}.{photo_format}"

    stream = io.BytesIO(request.FILES['photo'].read())
    photo = Image.open(stream)

    ftp = ftplib.FTP()

    ftp.connect('46.149.233.52', 30)
    ftp.login(os.environ['FTP_USER'], os.environ['FTP_PASSWORD'])
    ftp.cwd('ChildCard_images')

    src_rel = f'main/image/child_photo/user_{request.user.username}'
    src_abs = f'{ROOT_STATIC_APP}/{src_rel}'

    if f'user_{request.user.username}' not in os.listdir(f'{ROOT_STATIC_APP}/main/image/child_photo'):
        os.mkdir(src_abs)
    if f'user_{request.user.username}' not in ftp.nlst():
        ftp.mkd(f'user_{request.user.username}')
    ftp.cwd(f'user_{request.user.username}')

    photo = photo.resize((1200, 800))
    photo.save(f'{src_abs}/{photo_name}')

    ftp.storbinary(cmd=f"STOR {photo_name}", fp=open(f'{src_abs}/{photo_name}','rb'))

    ftp.close()

    child_card.path_child_photo = f"{src_rel}/{photo_name}"
    child_card.save()

    requests.post(url='https://lmfl1ie4pj.execute-api.us-east-1.amazonaws.com/api_sns/admin',
                  data=json.dumps({'Message': f"User {request.user.username} created card '{child_card.child_name}'"}))

    return redirect(request.POST['next'], request)


@login_required
def setting_account_form(request):
    cards = Card.objects.filter(creator_id=request.user)
    return render(request, 'main/setting_account.html', {'cards': cards})


def delete_card(card_id):
    card = Card.objects.get(global_id=card_id)
    card_name = card.child_name
    src_abs = f'{ROOT_STATIC_APP}/{card.path_child_photo}'
    os.remove(src_abs)

    _, username, photo_name = card.path_child_photo.rsplit('/', 2)

    ftp = ftplib.FTP()

    ftp.connect('46.149.233.52', 30)
    ftp.login(os.environ['FTP_USER'], os.environ['FTP_PASSWORD'])
    ftp.cwd('ChildCard_images')
    ftp.cwd(username)
    ftp.delete(photo_name)

    card.delete()

    return card_name


@login_required
def setting_account_complete(request):
    user = request.user
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.save()

    cards_id = request.POST.getlist('cards[]')
    cards = ""
    for card_id in cards_id:
        card_name = delete_card(card_id)
        cards += f" '{card_name}',"

    requests.post(url='https://lmfl1ie4pj.execute-api.us-east-1.amazonaws.com/api_sns/admin',
                  data=json.dumps({'Message': f"User {request.user.username} deleted cards [{cards[:-1]} ]"}))
    return redirect(request.POST['next'], request)


@login_required
def view_card(request):
    card = Card.objects.get(global_id=request.GET['card_id'])
    boy, girl = Card.BOY, Card.GIRL
    return render(request, 'main/view_card.html', {'card': card,
                                                   'boy': boy,
                                                   'girl': girl})


@login_required
def about(request):
    return render(request, 'main/about.html')


@login_required
def contact(request):
    return render(request, 'main/contact.html')


