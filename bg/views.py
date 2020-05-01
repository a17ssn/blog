from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from .models import Notes
from .forms import BlogForm
from django.contrib.auth.models import User

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




def blod_add(reqest):
    

    if reqest.method == 'POST':
        form = BlogForm(reqest.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = reqest.user
            new_form.save()
            return redirect('/blog')
        
    else:
        form = BlogForm()

    return render(reqest,"add.html",{'form' : form,})




def edit(reqest ,slug):
    editpage = get_object_or_404(Notes , slug=slug)
    if reqest.method == 'POST':
        form = BlogForm(reqest.POST , instance = editpage)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = reqest.user
            new_form.save()
            return redirect('/blog')
        
    else:
        form = BlogForm(instance = editpage)

    context={
        'form' : form
    }

    return render(reqest,"edit.html",context)




















