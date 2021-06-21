import json

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from siterysin.forms import PublicationForm, FormRegister
from siterysin.models import Publication, Album, Photo, FeedBack, CategoryFiles, File, SliderPhotos, Navigation, InfoStudent


def page(req):
    context = {'publics': Publication.objects.order_by('-id'),
               'slider_photos': SliderPhotos.objects.all(),
               'navs': Navigation.objects.all()}
    return render(req, 'page.html', context)


def pubcreate(req):
    data_response = {}
    if req.POST:
        pub = Publication.objects.create(title=req.POST.get('title'),
                                         text=req.POST.get('text'))
        pub.save()
        data_response.update({'title': pub.title, 'text': pub.text, 'pid': pub.id})
        form_photo = PublicationForm(req.POST, req.FILES, instance=pub)
        if form_photo.is_valid():
            form_photo.save()
        if pub.photo:
            data_response.update({'success': True, 'photo': pub.photo.url})
        else:
            data_response.update({'success': False})
    return HttpResponse(json.dumps(data_response), content_type='application/json')


def pubdel(req):
    data_response = {}
    if req.POST:
        pub_id = req.POST.get('pub_id')
        pub = Publication.objects.get(id=pub_id)
        pub.delete()
        data_response.update({'success': True})
    return HttpResponse(json.dumps(data_response), content_type='application/json')


def albums_page(req):
    albums = Album.objects.order_by('-id')
    context = {'albums': albums}
    return render(req, 'albums-page.html', context)


def album_page(req, aid):
    album = Album.objects.get(id=aid)
    context = {'album': album}
    return render(req, 'album.html', context)


def feedback_page(req):
    return render(req, 'feedback-page.html')


def add_feedback(req):
    data_response = {}
    if req.POST:
        feed = FeedBack.objects.create(title=req.POST.get('title'),
                                       text=req.POST.get('text'),
                                       email=req.POST.get('email'),
                                       full_name=req.POST.get('full_name'))
        feed.save()
        data_response.update({'success': True})
    return HttpResponse(json.dumps(data_response), content_type='application/json')


def categories_files(req):
    context = {'categories': CategoryFiles.objects.all()}
    return render(req, 'categories-page.html', context)


def category(req, categ_id):
    context = {'category': CategoryFiles.objects.get(id=categ_id)}
    return render(req, 'category.html', context)


def file(req, file_id):
    context = {'file': File.objects.get(id=file_id)}
    return render(req, 'file.html', context)


def search_page(req):
    query = req.GET.get('q')
    context = {}
    # search by categories
    categs = CategoryFiles.objects.filter(title__icontains=query)
    if categs.exists():
        context.update({'categs': categs})

    files = File.objects.filter(title__icontains=query)
    if files.exists():
        context.update({'files': files})

    pubs = Publication.objects.filter(title__icontains=query)
    if pubs.exists():
        context.update({'pubs': pubs})

    albums = Album.objects.filter(title__icontains=query)
    if albums.exists():
        context.update({'albums': albums})

    photos = Photo.objects.filter(description__icontains=query)
    if photos.exists():
        context.update({'photos': photos})

    return render(req, 'search-page.html', context)


def login_page(req):
    context = {}
    if req.user.is_authenticated:
        return redirect('startpage')
    else:
        if req.POST:
            username = req.POST.get('username')
            password = req.POST.get('password')
            user = authenticate(req,
                                username=username,
                                password=password)
            if user is not None:
                login(req, user)
                return redirect('startpage')
            else:
                context.update({'error': True})
    return render(req, 'login.html', context)


def logout_page(req):
    logout(req)
    return redirect('login-page')


def register_page(req):
    context = {}
    if req.POST:
        form = FormRegister(req.POST)
        if form.is_valid():
            new_stud = form.save()
            info_user = InfoStudent.objects.create(user=new_stud, group_name=req.POST.get('group_name'), school_name=req.POST.get('school_name'))
            info_user.save()
            return redirect('login-page')
        context.update({'form': form})
    return render(req, 'register-page.html', context)
