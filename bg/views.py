from django.shortcuts import render
from django.http import HttpResponse
from .models import Notes
# Create your views here.

def home_page(reqest):
    all_artical = Notes.objects.all()
    context = {
        'all_artical' : all_artical
    }
    return render(reqest,"blog.html" , context)





def singlePage(reqest , slug):
    artical = Notes.objects.get(slug=slug)
    context={
        'artical' : artical
    }
    return render(reqest,"single-page.html" , context)




def category(reqest):

    return render(reqest,"category.html")


























