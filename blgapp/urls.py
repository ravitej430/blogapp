from django.urls import path
from . views import *
urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('post/<int:pk>/',Detail.as_view(),name='post'),
    path('create/',Create.as_view(),name='create')
]
