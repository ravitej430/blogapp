from django .urls import path
from .views import *

urlpatterns = [
    path('',Signupview.as_view(),name='signup')
]

