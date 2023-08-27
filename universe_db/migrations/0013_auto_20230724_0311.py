from django.db import migrations, transaction

def PopulateSSP(apps, schema_editor):
    with transaction.atomic():
        SolarSystemPlanets = apps.get_model('universe_db', 'SolarSystemPlanets')
        SSPMeasurement = apps.get_model('universe_db', 'SSPMeasurement')
        Unit = apps.get_model('universe_db', 'Unit')

        # Create and Save units

        kg = Unit(name='kilogram', abbreviation='kg')     #mass
        kg.save()

        kg_m3 = Unit(name='kilogram per meter cubed', abbreviation='kg/m^3')    #density
        kg_m3.save()

        km = Unit(name='kilometer', abbreviation='km')      #diameter, distance, perihelion, aphelion,
        km.save()

        m_s2 = Unit(name='meter per second squared', abbreviation='m/s^2')  #gravity
        m_s2.save()

        m_s = Unit(name='meter per second', abbreviation='m/s')     #escape velocity
        m_s.save()

        hours = Unit(name='hours', abbreviation='hours')    #rotational period
        hours.save()

        days = Unit(name='days', abbreviation='days')    #orbital period
        days.save()

        degrees = Unit(name='degrees', abbreviation='degrees')    #orbital inclination,
        degrees.save()

        unitless= Unit(name='unitless', abbreviation='')    #eccentricity, number of moons
        unitless.save()

        C = Unit(name='temperature', abbreviation='C')    #mean temp
        C.save()

        bars = Unit(name='bars', abbreviation='bars')    #surface pressure
        bars.save()


        # Create and Save instances of planets

        mercury = SolarSystemPlanets(name='Mercury')
        mercury.save()

        venus = SolarSystemPlanets(name='Venus')
        venus.save()

        earth = SolarSystemPlanets(name='Earth')
        earth.save()

        mars = SolarSystemPlanets(name='Mars')
        mars.save()

        jupiter = SolarSystemPlanets(name='Jupiter')
        jupiter.save()

        saturn = SolarSystemPlanets(name='Saturn')
        saturn.save()

        uranus = SolarSystemPlanets(name='Uranus')
        uranus.save()

        neptune = SolarSystemPlanets(name='Neptune')
        neptune.save()

        pluto = SolarSystemPlanets(name='Pluto')
        pluto.save()


    # Create and save instances of SSPMeasurement linked to the planets

    #Mercury:
        SSPMeasurement(value=3.30e23, unit=kg, planet=mercury).save()        #mass
        SSPMeasurement(value=5429, unit=kg_m3, planet=mercury).save()        #density
        SSPMeasurement(value=4870, unit=km, planet=mercury).save()           #diameter
        SSPMeasurement(value=3.7, unit=m_s2, planet=mercury).save()          #gravity
        SSPMeasurement(value=4.3, unit=m_s, planet=mercury).save()           #escape velocity
        SSPMeasurement(value=5.79e7, unit=km, planet=mercury).save()         #distance
        SSPMeasurement(value=4.6e7, unit=km, planet=mercury).save()          #perihelion
        SSPMeasurement(value=6.98e7, unit=km, planet=mercury).save()         #aphelion
        SSPMeasurement(value=88, unit=days, planet=mercury).save()           #orbital period
        SSPMeasurement(value=1407.6, unit=hours, planet=mercury).save()      #rotational period
        SSPMeasurement(value=7.0, unit=degrees, planet=mercury).save()       #orbital inclination
        SSPMeasurement(value=0.206, unit=unitless, planet=mercury).save()    #eccentricity
        SSPMeasurement(value=167, unit=C, planet=mercury).save()             #mean temp
        SSPMeasurement(value=0, unit=bars, planet=mercury).save()            #surface pressure
        SSPMeasurement(value=0, unit=unitless, planet=mercury).save()        #number of moons



    #Venus:
        SSPMeasurement(value=4.87e24, unit=kg, planet=venus).save()          #mass
        SSPMeasurement(value=5243, unit=kg_m3, planet=venus).save()          #density
        SSPMeasurement(value=12104, unit=km, planet=venus).save()            #diameter
        SSPMeasurement(value=8.9, unit=m_s2, planet=venus).save()            #gravity
        SSPMeasurement(value=10.4, unit=m_s, planet=venus).save()            #escape velocity
        SSPMeasurement(value=1.082e8, unit=km, planet=venus).save()          #distance
        SSPMeasurement(value=1.075e8, unit=km, planet=venus).save()          #perihelion
        SSPMeasurement(value=1.089e8, unit=km, planet=venus).save()          #aphelion
        SSPMeasurement(value=224.7, unit=days, planet=venus).save()          #orbital period
        SSPMeasurement(value=-5832.5, unit=hours, planet=venus).save()       #rotational period
        SSPMeasurement(value=3.4, unit=degrees, planet=venus).save()         #orbital inclination
        SSPMeasurement(value=0.007, unit=unitless, planet=venus).save()      #eccentricity
        SSPMeasurement(value=464, unit=C, planet=venus).save()               #mean temp
        SSPMeasurement(value=92, unit=bars, planet=venus).save()             #surface pressure
        SSPMeasurement(value=0, unit=unitless, planet=venus).save()          #number of moons


    #Earth:
        SSPMeasurement(value=5.97e24, unit=kg, planet=earth).save()          #mass
        SSPMeasurement(value=5514, unit=kg_m3, planet=earth).save()          #density
        SSPMeasurement(value=12756, unit=km, planet=earth).save()            #diameter
        SSPMeasurement(value=9.8, unit=m_s2, planet=earth).save()            #gravity
        SSPMeasurement(value=11.2, unit=m_s, planet=earth).save()            #escape velocity
        SSPMeasurement(value=1.496e8, unit=km, planet=earth).save()          #distance
        SSPMeasurement(value=1.471e8, unit=km, planet=earth).save()          #perihelion
        SSPMeasurement(value=1.521e8, unit=km, planet=earth).save()          #aphelion
        SSPMeasurement(value=365.2, unit=days, planet=earth).save()          #orbital period
        SSPMeasurement(value=23.9, unit=hours, planet=earth).save()          #rotational period
        SSPMeasurement(value=0.0, unit=degrees, planet=earth).save()         #orbital inclination
        SSPMeasurement(value=0.017, unit=unitless, planet=earth).save()      #eccentricity
        SSPMeasurement(value=15, unit=C, planet=earth).save()                #mean temp
        SSPMeasurement(value=1, unit=bars, planet=earth).save()              #surface pressure
        SSPMeasurement(value=1, unit=unitless, planet=earth).save()          #number of moons


    #Mars:
        SSPMeasurement(value=6.42e23, unit=kg, planet=mars).save()           #mass
        SSPMeasurement(value=3934, unit=kg_m3, planet=mars).save()           #density
        SSPMeasurement(value=6792, unit=km, planet=mars).save()              #diameter
        SSPMeasurement(value=3.7, unit=m_s2, planet=mars).save()             #gravity
        SSPMeasurement(value=5.0, unit=m_s, planet=mars).save()              #escape velocity
        SSPMeasurement(value=2.280e8, unit=km, planet=mars).save()           #distance
        SSPMeasurement(value=2.067e8, unit=km, planet=mars).save()           #perihelion
        SSPMeasurement(value=2.493e8, unit=km, planet=mars).save()           #aphelion
        SSPMeasurement(value=687.0, unit=days, planet=mars).save()           #orbital period
        SSPMeasurement(value=24.6, unit=hours, planet=mars).save()           #rotational period
        SSPMeasurement(value=1.8, unit=degrees, planet=mars).save()          #orbital inclination
        SSPMeasurement(value=0.094, unit=unitless, planet=mars).save()       #eccentricity
        SSPMeasurement(value=-65, unit=C, planet=mars).save()                #mean temp
        SSPMeasurement(value=.01, unit=bars, planet=mars).save()             #surface pressure
        SSPMeasurement(value=2, unit=unitless, planet=mars).save()           #number of moons

    #Jupiter:
        SSPMeasurement(value=1.898e27, unit=kg, planet=jupiter).save()       #mass
        SSPMeasurement(value=1326, unit=kg_m3, planet=jupiter).save()        #density
        SSPMeasurement(value=142984, unit=km, planet=jupiter).save()         #diameter
        SSPMeasurement(value=23.1, unit=m_s2, planet=jupiter).save()         #gravity
        SSPMeasurement(value=59.5, unit=m_s, planet=jupiter).save()          #escape velocity
        SSPMeasurement(value=7.785e8, unit=km, planet=jupiter).save()        #distance
        SSPMeasurement(value=7.406e8, unit=km, planet=jupiter).save()        #perihelion
        SSPMeasurement(value=8.164e8, unit=km, planet=jupiter).save()        #aphelion
        SSPMeasurement(value=4331, unit=days, planet=jupiter).save()         #orbital period
        SSPMeasurement(value=9.9, unit=hours, planet=jupiter).save()         #rotational period
        SSPMeasurement(value=1.3, unit=degrees, planet=jupiter).save()       #orbital inclination
        SSPMeasurement(value=0.049, unit=unitless, planet=jupiter).save()    #eccentricity
        SSPMeasurement(value=-110, unit=C, planet=jupiter).save()            #mean temp
        SSPMeasurement(value=None, unit=unitless, planet=jupiter).save()     #surface pressure
        SSPMeasurement(value=92, unit=unitless, planet=jupiter).save()       #number of moons

    #Saturn:
        SSPMeasurement(value=5.680e26, unit=kg, planet=saturn).save()        #mass
        SSPMeasurement(value=687, unit=kg_m3, planet=saturn).save()          #density
        SSPMeasurement(value=120536, unit=km, planet=saturn).save()          #diameter
        SSPMeasurement(value=9.0, unit=m_s2, planet=saturn).save()           #gravity
        SSPMeasurement(value=35.5, unit=m_s, planet=saturn).save()           #escape velocity
        SSPMeasurement(value=1.432e9, unit=km, planet=saturn).save()         #distance
        SSPMeasurement(value=1.3576e9, unit=km, planet=saturn).save()        #perihelion
        SSPMeasurement(value=1.5065e9, unit=km, planet=saturn).save()        #aphelion
        SSPMeasurement(value=10747, unit=days, planet=saturn).save()         #orbital period
        SSPMeasurement(value=10.7, unit=hours, planet=saturn).save()         #rotational period
        SSPMeasurement(value=2.5, unit=degrees, planet=saturn).save()        #orbital inclination
        SSPMeasurement(value=0.052, unit=unitless, planet=saturn).save()     #eccentricity
        SSPMeasurement(value=--140, unit=C, planet=saturn).save()            #mean temp
        SSPMeasurement(value=None, unit=unitless, planet=saturn).save()      #surface pressure
        SSPMeasurement(value=83, unit=unitless, planet=saturn).save()        #number of moons


    #Uranus:
        SSPMeasurement(value=8.66e25, unit=kg, planet=uranus).save()         #mass
        SSPMeasurement(value=1270, unit=kg_m3, planet=uranus).save()         #density
        SSPMeasurement(value=51118, unit=km, planet=uranus).save()           #diameter
        SSPMeasurement(value=8.7, unit=m_s2, planet=uranus).save()           #gravity
        SSPMeasurement(value=21.3, unit=m_s, planet=uranus).save()           #escape velocity
        SSPMeasurement(value=2.867e9, unit=km, planet=uranus).save()         #distance
        SSPMeasurement(value=2.7327e9, unit=km, planet=uranus).save()        #perihelion
        SSPMeasurement(value=3.0014e9, unit=km, planet=uranus).save()        #aphelion
        SSPMeasurement(value=30589, unit=days, planet=uranus).save()         #orbital period
        SSPMeasurement(value=-17.2, unit=hours, planet=uranus).save()        #rotational period
        SSPMeasurement(value=0.8, unit=degrees, planet=uranus).save()        #orbital inclination
        SSPMeasurement(value=0.047, unit=unitless, planet=uranus).save()     #eccentricity
        SSPMeasurement(value=-195, unit=C, planet=uranus).save()             #mean temp
        SSPMeasurement(value=None, unit=unitless, planet=uranus).save()      #surface pressure
        SSPMeasurement(value=27, unit=unitless, planet=uranus).save()        #number of moons


    #Neptune:
        SSPMeasurement(value=1.02e26, unit=kg, planet=neptune).save()        #mass
        SSPMeasurement(value=1638, unit=kg_m3, planet=neptune).save()        #density
        SSPMeasurement(value=49528, unit=km, planet=neptune).save()          #diameter
        SSPMeasurement(value=11.0, unit=m_s2, planet=neptune).save()         #gravity
        SSPMeasurement(value=23.5, unit=m_s, planet=neptune).save()          #escape velocity
        SSPMeasurement(value=4.515e9, unit=km, planet=neptune).save()        #distance
        SSPMeasurement(value=4.4711e9, unit=km, planet=neptune).save()       #perihelion
        SSPMeasurement(value=4.5589e9, unit=km, planet=neptune).save()       #aphelion
        SSPMeasurement(value=59800, unit=days, planet=neptune).save()        #orbital period
        SSPMeasurement(value=16.1, unit=hours, planet=neptune).save()        #rotational period
        SSPMeasurement(value=1.8, unit=degrees, planet=neptune).save()       #orbital inclination
        SSPMeasurement(value=0.010, unit=unitless, planet=neptune).save()    #eccentricity
        SSPMeasurement(value=-200, unit=C, planet=neptune).save()            #mean temp
        SSPMeasurement(value=None, unit=unitless, planet=neptune).save()     #surface pressure
        SSPMeasurement(value=14, unit=unitless, planet=neptune).save()       #number of moons


    #Pluto (even though not a planet):
        SSPMeasurement(value=1.30e22, unit=kg, planet=pluto).save()        #mass
        SSPMeasurement(value=1850, unit=kg_m3, planet=pluto).save()        #density
        SSPMeasurement(value=2376, unit=km, planet=pluto).save()           #diameter
        SSPMeasurement(value=0.7, unit=m_s2, planet=pluto).save()          #gravity
        SSPMeasurement(value=1.3, unit=m_s, planet=pluto).save()           #escape velocity
        SSPMeasurement(value=5.9064e9, unit=km, planet=pluto).save()       #distance
        SSPMeasurement(value=4.4368e9, unit=km, planet=pluto).save()       #perihelion
        SSPMeasurement(value=7.3759e9, unit=km, planet=pluto).save()       #aphelion
        SSPMeasurement(value=90560, unit=days, planet=pluto).save()        #orbital period
        SSPMeasurement(value=-153.3, unit=hours, planet=pluto).save()      #rotational period
        SSPMeasurement(value=17.2, unit=degrees, planet=pluto).save()      #orbital inclination
        SSPMeasurement(value=0.244, unit=unitless, planet=pluto).save()    #eccentricity
        SSPMeasurement(value=-225, unit=C, planet=pluto).save()           #mean temp
        SSPMeasurement(value=0.00001, unit=bars, planet=pluto).save()      #surface pressure
        SSPMeasurement(value=5, unit=unitless, planet=pluto).save()        #number of moons


    SSPMeasurement.objects.filter(value=None).update(value=0.0)

def ReverseSSP(apps, schema_editor):
    SolarSystemPlanets = apps.get_model('universe_db', 'SolarSystemPlanets')
    SSPMeasurement = apps.get_model('universe_db', 'SSPMeasurement')
    Unit = apps.get_model('universe_db', 'Unit')

    SolarSystemPlanets.objects.all().delete()
    SSPMeasurement.objects.all().delete()
    Unit.objects.all().delete()

class Migration(migrations.Migration):

    initial = True
    dependencies = [ ("universe_db", "0001_initial"), ]

    operations = [migrations.RunPython(PopulateSSP), ]
