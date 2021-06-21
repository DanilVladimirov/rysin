import os
import random
from django.contrib.auth.models import User
from django.db import models


def file_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    return f'{basefilename}_{randomstr}{file_extension}'


class Publication(models.Model):
    title = models.CharField(max_length=100, default='no-title', blank=True)
    text = models.TextField(default='no-text', blank=True)
    photo = models.ImageField(default=None, null=True, blank=True, upload_to=file_path)

    def __str__(self):
        return self.title


class Photo(models.Model):
    photo = models.ImageField(default=None, null=True, blank=True, upload_to=file_path)
    description = models.CharField(max_length=50, default='', blank=True)

    def __str__(self):
        return self.description


class Album(models.Model):
    title = models.CharField(max_length=50, default='', blank=True)
    photo_title = models.ImageField(default=None, null=True, blank=True, upload_to=file_path)
    photos = models.ManyToManyField(Photo)

    def __str__(self):
        return self.title


class FeedBack(models.Model):
    full_name = models.CharField(max_length=200, default='noname')
    email = models.EmailField(default='nomail')
    text = models.TextField(default='')
    title = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.title


class File(models.Model):
    title = models.CharField(max_length=100, default='notitle')
    file = models.FileField(null=True, blank=True, upload_to=file_path)

    def __str__(self):
        return self.title


class CategoryFiles(models.Model):
    title = models.CharField(max_length=100, default='notitle')
    files = models.ManyToManyField(File)

    def __str__(self):
        return self.title


class SliderPhotos(models.Model):
    photo = models.ImageField(null=True, blank=True, upload_to=file_path)

    def __str__(self):
        return f'{self.id}'


class Navigation(models.Model):
    title = models.CharField(max_length=50, default='')
    url = models.URLField()

    def __str__(self):
        return self.title


class InfoStudent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    group_name = models.CharField(max_length=100, default='')
    school_name = models.CharField(max_length=200, default='')

