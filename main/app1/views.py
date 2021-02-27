from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Image, Category


def home_page(request):
    images = Image.objects.all()
    c = Category.objects.all()
    return render(request,'home.html',{'im': images, 'cat': c})


def category_page(request,id):
        c = Category.objects.all()
        cid=Category.objects.get(pk=id)       # cid is category ID
        images=Image.objects.filter(categ=cid)
        return render(request, 'home.html', {'im': images, 'cat': c})


