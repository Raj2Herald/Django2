from django.urls import path
from .views import *

urlpatterns = [
    path('airports/',view_get_post_airport),
    path('airports/<int:ID>',view_getByID_updateByID_deleteByID),
]