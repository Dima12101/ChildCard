import os
import io
import ftplib

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required

from django.utils import timezone

from .models import Card

from PIL import Image

ROOT_STATIC_APP = f'{settings.PROJECT_ROOT}/static/main'


@login_required
def index(request):
    cards_data = Card.objects.filter(creator_id=request.user)
    indexes = range(len(cards_data))
    return render(request, 'main/index.html', {'cards_data': cards_data, 'indexes': indexes})


@login_required
def create_card_form(request):
    return render(request, 'main/create_card.html')
	

@login_required
def create_card_complete(request):

    photo_name = request.FILES['photo'].name
    if not photo_name.split('.')[-1] in ['jpg', 'png']:
        return render(request, 'main/create_card.html')

    stream = io.BytesIO(request.FILES['photo'].read())
    photo = Image.open(stream)

    ftp = ftplib.FTP()

    ftp.connect('46.149.233.52', 30)
    ftp.login(os.environ['FTP_USER'], os.environ['FTP_PASSWORD'])
    ftp.cwd('ChildCard_images')


    src_rel = f'image/child_photo/user_{request.user.username}'
    src_abs = f'{ROOT_STATIC_APP}/{src_rel}'

    if f'user_{request.user.username}' not in os.listdir(f'{ROOT_STATIC_APP}/image/child_photo'):
        os.mkdir(src_abs)
    if f'user_{request.user.username}' not in ftp.nlst():
        ftp.mkd(f'user_{request.user.username}')
    ftp.cwd(f'user_{request.user.username}')

    photo = photo.resize((1200, 800))
    photo.save(f'{src_abs}/{photo_name}')

    ftp.storbinary(cmd=f"STOR {photo_name}", fp=open(f'{src_abs}/{photo_name}','rb'))

    child_card = Card(
        child_name=request.POST['childname'],
        creator_id=request.user,
        path_child_photo=f'main/{src_rel}/{photo_name}',
    )
    child_card.save()
    ftp.close()

    return redirect(request.POST['next'], request)


@login_required
def about(request):
    return render(request, 'main/about.html')


@login_required
def contact(request):
    return render(request, 'main/contact.html')


