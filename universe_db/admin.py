from django.contrib import admin
from .models import SolarSystemPlanets, Unit, SSPMeasurement, PlanetarySystems

#admin.site.register(Article)

#@admin.register(SolarSystemPlanets)    #Registers 'SolarSytemPlanets' on the admin site

class SSPModel(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']

admin.site.register(Unit)
admin.site.register(SolarSystemPlanets, SSPModel)
admin.site.register(SSPMeasurement)
admin.site.register(PlanetarySystems)
