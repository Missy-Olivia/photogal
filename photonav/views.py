from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt


# Create your views here.
def gallery(request):
    images = Image.objects.all()
    categories = Category.objects.all()
    locations = Locations.objects.all()
    return render(request, 'index.html', {"images":images, "categories":categories, "locations":locations})