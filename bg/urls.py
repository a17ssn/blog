from django.urls import path
from .views import home_page , singlePage , category ,blod_add ,edit

app_name = 'bg'


urlpatterns = [
    path('',home_page , name='home'),

    path('category/', category , name = 'category' ),
    path('add/', blod_add , name = 'blod_add' ),
    path('<slug:slug>/', singlePage , name = 'blog_Page' ),
    path('<slug:slug>/edit', edit , name = 'edit' ),



]

