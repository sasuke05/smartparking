from django.urls import path
from . import views
urlpatterns=[
    path('',views.home, name = 'home'),
    path('confirmation',views.home, name = 'confirmation')
]