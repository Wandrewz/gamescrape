from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contactus'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.details, name='details')

]