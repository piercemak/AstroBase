from django.urls import path
from . import views

app_name = 'universe_db'

urlpatterns = [
    path('', views.homepage, name='homepage'),

    path('planets/', views.planet_list, name='planet_list'),

    path('planets/<str:planet_name>/', views.planet_detail, name='planet_detail'),

    path('exoplanets/', views.exoplanets, name='exoplanets'),

    path('planetary-systems/', views.planetary_systems, name='planetary_systems'),

    path('calculate/', views.calculate, name='calculate'),

    #.as_view() is used because Django's URL routing expects a function and not a class
    path('planet-autocomplete/', views.PlanetAutocomplete.as_view(), name='planet-autocomplete', ),
    path('planetary-system-autocomplete/', views.PlanetarySystemAutocomplete.as_view(), name='planetary-system-autocomplete', ),

    path('mars_photos/', views.mars_photos, name='mars_photos'),

    path('nasa_photos/', views.nasa_photos, name='nasa_photos'),



]


