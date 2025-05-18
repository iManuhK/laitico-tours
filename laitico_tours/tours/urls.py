from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('destinations/', views.destinations, name='destinations'),
    path('destinations/<str:slug>/', views.destination_detail, name='destination_detail'),
    path('destinations/<str:slug>/book', views.book_tour, name='book_tour'),
    path('about/', views.about, name='about'),
    path('tailor-your-package/', views.tailoredPackages, name='packages'),
    path('contact-us/', views.contact, name='contact'),
]
