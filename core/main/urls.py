from django.urls import path
from .import views



urlpatterns = [
    path('',views.homeListView.as_view(),name ='index'),
    path('services/',views.serviceListView.as_view(), name = 'service'),
    path('about/',views.aboutListView.as_view(),name = 'aboutus'),
    path('contact/',views.contactListView.as_view(),name = 'contactus')
]