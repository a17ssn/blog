from django.urls import path
from .views import home_page , singlePage , category

app_name = 'bg'


urlpatterns = [
    path('',home_page , name='home'),
    path('<slug:slug>/', singlePage , name = 'blog_Page' ),
    path('category/', category , name = 'category' ),

]

