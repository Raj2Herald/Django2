from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('hello/',view_hello_world),
    path('test',view_hello_world_template),
    path('helloworld/',view_hello_world_test),
    path('flights/',view_flights_page)
    path('flightdata/',view_flight_lists),
    path('flightform/',view_fight_form),
    path('flightform/save',view_flightdata_save),
    path('flightdata/edit/<int:ID>',view_flightdata_updateform),
    path('flightdata/edit/update/<int:ID>',view_update_form_data_in_db),
    path('signup/',view_register_user),
    path('restrictpage/',view_hello_world),
    


   
]