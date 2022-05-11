from django.urls import path
from .views import *
urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('post/<int:pk>/',Detail.as_view(),name='post'),
    path('post/',Create.as_view(),name='create'),
    path('post/<int:pk>/edit/',Blogupdateview.as_view(),name='postedit'),
    path('post/<int:pk>/delete/',DeleteView.as_view(),name='delete')
]