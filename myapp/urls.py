from django.urls import path
from . import views



urlpatterns=[
    path('',views.home,name='my_home'),
    path('mimi/',views.about,name='about_us'),
    path('contact/',views.contact, name='contact_us'),
    path('services/',views.services, name='services'),
    path('Blog/',views.blog, name='blog'),
]